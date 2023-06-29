from odoo import models,fields 
class estate_property_offer(models.Model):

    _name = "estate.property.offer"
    _description = 'Property offer'
    _log_access=False

    price = fields.Float("price",required=True)
    status = fields.Selection(selection=[("a", "Accepted"),("r", "Refused"),],string="Status",copy=False,default='A')
    partner_id = fields.Many2one("res.partner",string="partner",required=True)
    property_id = fields.Many2one("estate.property",string="property",required=True)
    





