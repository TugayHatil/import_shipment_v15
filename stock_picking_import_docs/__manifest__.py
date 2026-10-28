# SPDX-License-Identifier: LicenseRef-Projet-Proprietary
#
# Copyright (c) 2026 Projet İş Çözümleri Limited Şirketi
#
# This file is part of a proprietary Odoo addon.
# Use of this file is governed by the LICENSE file included
# in the root of this repository.
{
    'name': 'Stock Picking: Import Documents',
    'version': '15.0.1.7.0',
    'category': 'Inventory',
    'summary': 'Import documents (invoice, packing list, bill of lading, customs declaration) on transfers',
    'author': 'Projet İş Çözümleri Ltd. Şti.',
    'website': 'https://projet.solutions',
    'license': 'Other proprietary',
    'maintainer': 'Projet İş Çözümleri Ltd. Şti.',
    'depends': [
        'stock',
    ],
    'data': [
        'security/res_groups.xml',
        'views/stock_picking_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'stock_picking_import_docs/static/src/scss/import_docs.scss',
            'stock_picking_import_docs/static/src/js/import_docs_multi.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
