from odoo import api,fields,models
from odoo.exceptions import UserError

class EstatePropertyWizard(models.TransientModel):
    _name = "estate.property.wizard"
    _description ="Wizard"


    price = fields.Float("price", required=True)
    offer_status = fields.Selection(selection=[(
        "A", "Accepted"), ("R", "Refused"),], string="Status", copy=False)
    buyer = fields.Many2one('res.partner', string="Buyer", copy=False,tracking=True)
    
    def _get_default_property(self):
        return self.env['estate.property'].browse(self.env.context.get('active_ids'))

    property_ids=fields.Many2many('estate.property',string="estateeee",default=_get_default_property)

    
    def action_add_offer(self):
        # for i in self:
        if self.offer_status == 'A':
            self.offer_status='A'