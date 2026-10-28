# -*- coding: utf-8 -*-
{
    'name': 'Stock Picking Import Documents',
    'version': '15.0.1.1.0',
    'category': 'Inventory',
    'summary': 'Attach and preview import documents (invoice, packing list, bill of lading) on transfers',
    'description': """
        Adds an "Import" tab on stock transfers where authorized users can
        attach multiple files per document type - import invoice, packing
        list, bill of lading and customs declaration. Files show up as
        attachment icon blocks and open inline in a new tab for preview
        without downloading. They also appear in the chatter attachments.
        The tab and the fields are restricted to the "Import Documents
        Manager" group.
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
            'stock_picking_import_docs/static/src/js/import_docs_multi.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
