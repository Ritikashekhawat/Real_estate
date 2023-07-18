from odoo import models, fields, Command
from odoo.exceptions import UserError


class EstateProperty(models.Model):

    _name = 'estate.property'
    _inherit = "estate.property"

    def action_sold(self):
        print("-----------------------")

        self.env['project.project'].create(
            
        )
        return super().action_sold()
