# -*- coding: utf-8 -*-
{
    'name': "Study Project",
    'version': '0.1',
    'summary': "Enmasys Project Management",
    'sequence': -100,
    'description': "Enmasys Project Management",
    'website': "https://www.odoo.com/page/billing",
    'category': 'Productivity',
    'depends': [
        'sale',
        'mail',
        'sale',
        'website_slides',
        'hr'
    ],
    'data': [
        'security\ir.model.access.csv',
        'views\project_study.xml',
        'views\sale.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_isntall': False,
}