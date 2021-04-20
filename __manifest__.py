# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Diet',
    'version': '1.0',
    'summary': 'Nutrition and diet',
    'sequence': 10,
    'description': "Nutrition and diet",
    'category': 'Nutrition',
    'author': 'Alberto Rubio',
    'depends': ['base','web'],
    'data': [
        "security/ir.model.access.csv",
        "views/diet_view.xml",
        "views/templates.xml",
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
