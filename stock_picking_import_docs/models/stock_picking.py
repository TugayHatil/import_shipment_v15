# -*- coding: utf-8 -*-
from odoo import fields, models

IMPORT_DOCS_GROUP = 'stock_picking_import_docs.group_import_docs_manager'


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    import_invoice_file = fields.Binary(
        string='Import Invoice',
        attachment=True,
        groups=IMPORT_DOCS_GROUP,
    )
    import_invoice_filename = fields.Char(
        string='Import Invoice Filename',
        groups=IMPORT_DOCS_GROUP,
    )
    packing_list_file = fields.Binary(
        string='Packing List',
        attachment=True,
        groups=IMPORT_DOCS_GROUP,
    )
    packing_list_filename = fields.Char(
        string='Packing List Filename',
        groups=IMPORT_DOCS_GROUP,
    )
    bill_of_lading_file = fields.Binary(
        string='Bill of Lading',
        attachment=True,
        groups=IMPORT_DOCS_GROUP,
    )
    bill_of_lading_filename = fields.Char(
        string='Bill of Lading Filename',
        groups=IMPORT_DOCS_GROUP,
    )
