# -*- coding: utf-8 -*-
{
    'name': 'Stock Picking Import Documents',
    'version': '15.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Attach and preview import documents (invoice, packing list, bill of lading) on transfers',
    'description': """
        Adds an "Import" tab on stock transfers where authorized users can
        attach three import documents - import invoice, packing list and
        bill of lading - and preview the PDF files directly in the form
        without downloading them. The tab and the fields are restricted
        to the "Import Documents Manager" group.
    """,
    'author': 'Tugay Hatil',
    'website': 'https://github.com/TugayHatil',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'security/res_groups.xml',
        'views/stock_picking_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'stock_picking_import_docs/static/src/scss/pdf_viewer.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
