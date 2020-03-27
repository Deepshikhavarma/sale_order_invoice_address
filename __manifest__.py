# -*- coding: utf-8 -*-
{
    'name': "Sale Order Invoice Address",

    'summary': """
        This module displays child contacts of parent contact in invoice and delivery address""",

    'description': """
        This module displays child contacts of parent contact in invoice and delivery address on
        checking the customer, invoice address and delivery address in sales configuration settings.

    """,

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/resconfig.xml',
        'views/saleorder.xml',
    ],
    
}