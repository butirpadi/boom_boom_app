# -*- coding: utf-8 -*-
{
    'name': "BoombaSys",

    'summary': """
        Application for manage Water Park/Water Boom on Indonesia""",

    'description': """
        Application for manage Water Park/Water Boom on Indonesia
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'point_of_sale', 'purchase', 'stock', 'default_setting_for_indonesian_app'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_default_data.xml',
        'views/membership_view.xml',
        'views/ticketing_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}