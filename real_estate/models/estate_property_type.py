from odoo import  api,models,fields 

class estate_property_type(models.Model):

    _name = "estate.property.type"
    _description = 'Property Type'
    _log_access=False
    _order="name"

    name = fields.Char("Property Type", required=True)
    property_ids=fields.One2many("estate.property","property_type_id",string="Properties")
    sequence = fields.Integer('Sequence')
    
    offer_ids = fields.One2many("estate.property.offer",'property_type_id',compute="_compute_offer_count",string="Offers_IDS")
    offer_count=fields.Integer(compute="_compute_offer_count")

    _sql_contraints=[('property_Type_name_unq','unique (name)',"A property type name must be unique")]
 

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for OC in self:
            OC.offer_count=len(OC.offer_ids)
    
