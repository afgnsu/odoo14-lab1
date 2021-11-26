# -*- coding: utf-8 -*-
{
    'name': "Lab1(學生成績系統)",

    'summary': "多個Model、視圖的Menu和View分離",

    'description': "介吾測試",

    'author': "蘇介吾",
    'website': "http://afgn.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/lab1_class.xml',
        'views/lab1_score.xml',
        'views/lab1_student.xml',
        'views/lab1_teacher.xml',
        'views/lab1_menu.xml',
    ],
    # only loaded in demonstration mode
    #'demo': ['demo/demo.xml'],
}
