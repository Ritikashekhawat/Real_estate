from odoo import api, fields, models
from odoo.exceptions import UserError


class EstatePropertyWizard(models.TransientModel):
    _name = "estate.property.wizard"
    _description = "Estate Wizard"

    price = fields.Float('Price')
    validity = fields.Integer("Validity")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)

    def make_offer(self):
        select_propert_id = self.env.context.get('active_ids', [])
        offers = self.env['estate.property.offer']
        for pro_i in select_propert_id:
            offer_ids = {
                'property_id': pro_i,
                'price': self.price,
                'Validity': self.validity,
                'partner_id': self.buyer_id.id
            }
        offers.create(offer_ids)