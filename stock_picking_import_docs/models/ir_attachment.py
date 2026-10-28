# SPDX-License-Identifier: LicenseRef-Projet-Proprietary
#
# Copyright (c) 2026 Projet İş Çözümleri Limited Şirketi
#
# This file is part of a proprietary Odoo addon.
# Use of this file is governed by the LICENSE file included
# in the root of this repository.
from odoo import api, fields, models


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    import_invoice_picking_ids = fields.Many2many(
        'stock.picking',
        'picking_import_invoice_attachment_rel',
        'attachment_id',
        'picking_id',
    )
    packing_list_picking_ids = fields.Many2many(
        'stock.picking',
        'picking_packing_list_attachment_rel',
        'attachment_id',
        'picking_id',
    )
    bill_of_lading_picking_ids = fields.Many2many(
        'stock.picking',
        'picking_bill_of_lading_attachment_rel',
        'attachment_id',
        'picking_id',
    )
    customs_declaration_picking_ids = fields.Many2many(
        'stock.picking',
        'picking_customs_declaration_attachment_rel',
        'attachment_id',
        'picking_id',
    )
    import_doc = fields.Boolean(
        compute='_compute_import_doc',
        store=True,
    )

    @api.depends(
        'import_invoice_picking_ids',
        'packing_list_picking_ids',
        'bill_of_lading_picking_ids',
        'customs_declaration_picking_ids',
    )
    def _compute_import_doc(self):
        for attachment in self:
            attachment.import_doc = bool(
                attachment.import_invoice_picking_ids
                or attachment.packing_list_picking_ids
                or attachment.bill_of_lading_picking_ids
                or attachment.customs_declaration_picking_ids
            )
