{
    'name' : 'Real Estate',
    'summary': "Real Estate App",
    'author': "Odoo",
    
    'depends' : ['base'],
    'application': True,
    'installable':True,
    
    'data':[
     'security/ir.model.access.csv',
     'view/estate_property_tag.xml',
     'view/estate_property_type.xml',
     'view/estate_property_views.xml',
    ]
}