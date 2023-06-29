from odoo import models,fields 
class estate_property_type(models.Model):

    _name = "estate.property.type"
    _description = 'Property Type'
    _log_access=False

    name = fields.Char("Property Type", required=True)
    property_ids=fields.One2many("estate.property","property_type_id",string="Properties")
