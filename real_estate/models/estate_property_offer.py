from odoo import models,fields 
class estate_property_offer(models.Model):

    _name = "estate.property.offer"
    _description = 'Property offer'
    _log_access=False

    price = fields.Float("price", required=True)
    state = fields.Selection(selection=[("A", "Accepted"),("R", "Refused"),],string="Status",copy=False,default=False,)
    partner_id = fields.Many2one("res.partner",required=True)


