{
    'name': 'Estate Account',
    'summary': "Estate Account App",
    'author': "Odoo",

    'installable': True,
    'application': True,

    'depends': ['real_estate',
                'account'],

    'data': [
        'report/estate_reports.xml',
    ],

    'auto_install': True

}
