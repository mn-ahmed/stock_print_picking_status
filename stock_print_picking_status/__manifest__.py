# Copyright 2022 Sodexis
# License OEEL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Stock Print Picking Status",
    'summary': """

        This module will add tracking of printed field once the picking is printed
         """,
    'version': "15.0.2.0.0",
    'category': 'Uncategorized',
    'website': "http://sodexis.com/",
    'author': "Sodexis",
    'license': 'OEEL-1',
    'installable': True,
    'application': False,
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_picking_view.xml',    
        'report/stock_picking_report.xml',
    ],
    "cloc_exclude": [
        "**/*", # can be used to ignore an entire module.
    ]
}
