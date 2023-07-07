from odoo import models,fields 
class estate_property_tag(models.Model):

    _name = "estate.property.tag"
    _description = 'Property Tag'
    _log_access=False
    _order="name"

    name = fields.Char("Property Tag", required=True)
    color=fields.Integer("color")
    
    _sql_constraints = [ ('Property_tag_unq','UNIQUE (name)','A property tag name must be unique')]
