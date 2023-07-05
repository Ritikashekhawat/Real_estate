from odoo import models,fields 
class estate_property_tag(models.Model):

    _name = "estate.property.tag"
    _description = 'Property Tag'
    _log_access=False

    name = fields.Char("Property Tag", required=True)

    _sql_constraints = [ ('name_unq','UNIQUE (name)','An offer price must be strictly positive')]
