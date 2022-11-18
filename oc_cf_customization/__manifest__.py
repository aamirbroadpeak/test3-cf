# -*- coding: utf-8 -*-
{
    'name': "Capital Fish Customization",

    'summary': """Custom Development""",

    'description': """This module contains all development work related to Capital Fish project
    """,

    'author': "Odoo Concepts",
    'website': "https://www.odooconcepts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','purchase'],

    # always loaded
    'data': [
        'security\ir.model.access.csv',
        'views\sale_report_inherit.xml',
        'views\purchase_report_inherit.xml',
        'wizard\purchase_order_wizard_view.xml',
        'views\purchase_order_menu.xml',
        'report\cf_reports.xml',
        'report\purchase_order_details.xml',
    ],
}
