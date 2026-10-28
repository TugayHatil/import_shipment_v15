# SPDX-License-Identifier: LicenseRef-Projet-Proprietary
#
# Copyright (c) 2026 Projet İş Çözümleri Limited Şirketi
#
# This file is part of a proprietary Odoo addon.
# Use of this file is governed by the LICENSE file included
# in the root of this repository.
from odoo import fields, models

IMPORT_DOCS_GROUP = 'stock_picking_import_docs.group_import_docs_manager'


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    import_invoice_attachment_ids = fields.Many2many(
        'ir.attachment',
        'picking_import_invoice_attachment_rel',
        'picking_id',
        'attachment_id',
        string='Import Invoice',
        groups=IMPORT_DOCS_GROUP,
    )
    packing_list_attachment_ids = fields.Many2many(
        'ir.attachment',
        'picking_packing_list_attachment_rel',
        'picking_id',
        'attachment_id',
        string='Packing List',
        groups=IMPORT_DOCS_GROUP,
    )
    bill_of_lading_attachment_ids = fields.Many2many(
        'ir.attachment',
        'picking_bill_of_lading_attachment_rel',
        'picking_id',
        'attachment_id',
        string='Bill of Lading',
        groups=IMPORT_DOCS_GROUP,
    )
    customs_declaration_attachment_ids = fields.Many2many(
        'ir.attachment',
        'picking_customs_declaration_attachment_rel',
        'picking_id',
        'attachment_id',
        string='Customs Declaration',
        groups=IMPORT_DOCS_GROUP,
    )
