# SPDX-License-Identifier: LicenseRef-Projet-Proprietary
#
# Copyright (c) 2026 Projet İş Çözümleri Limited Şirketi
#
# This file is part of a proprietary Odoo addon.
# Use of this file is governed by the LICENSE file included
# in the root of this repository.
import base64
import json
import logging
import unicodedata

from odoo import _, http
from odoo.exceptions import AccessError
from odoo.http import request

_logger = logging.getLogger(__name__)


class ImportDocsBinary(http.Controller):

    @http.route('/stock_picking_import_docs/upload', type='http', auth='user')
    def upload(self, ufile, callback=None):
        """Upload import documents without linking them to a record, so they
        stay out of the chatter attachment list. Mirrors the response format
        of /web/binary/upload_attachment."""
        if not request.env.user.has_group(
                'stock_picking_import_docs.group_import_docs_manager'):
            raise AccessError(_("You are not allowed to upload import documents."))
        files = request.httprequest.files.getlist('ufile')
        Attachment = request.env['ir.attachment']
        out = """<script language="javascript" type="text/javascript">
                    var win = window.top.window;
                    win.jQuery(win).trigger(%s, %s);
                </script>"""
        args = []
        for ufile in files:
            filename = ufile.filename
            if request.httprequest.user_agent.browser == 'safari':
                # Safari sends NFD UTF-8 (where é is composed by 'e' and [accent])
                # we need to send it the same stuff, otherwise it'll fail
                filename = unicodedata.normalize('NFD', ufile.filename)
            try:
                attachment = Attachment.create({
                    'name': filename,
                    'datas': base64.encodebytes(ufile.read()),
                })
            except AccessError:
                args.append({'error': _("You are not allowed to upload an attachment here.")})
            except Exception:
                args.append({'error': _("Something horrible happened")})
                _logger.exception("Fail to upload attachment %s", ufile.filename)
            else:
                args.append({
                    'filename': filename.replace('\x00', ''),
                    'mimetype': ufile.content_type,
                    'id': attachment.id,
                    'size': attachment.file_size,
                })
        return out % (json.dumps(callback), json.dumps(args)) if callback else json.dumps(args)
