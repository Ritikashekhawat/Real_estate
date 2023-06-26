{
    'name' : 'Real Estate',
    'summary': "Real Estate App",
    'author': "Odoo",
    
    #'depends' : ['base_setup', 'product', 'analytic', 'portal', 'digest'],
    'application': True,
    'installable':True,
    
    'data':[
     'security/ir.model.access.csv',
     'views/estate_view.xml'
    ]
}