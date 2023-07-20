from odoo import models, fields, Command
from odoo.exceptions import UserError


class EstateProperty(models.Model):

    _name = 'estate.property'
    _inherit = "estate.property"

    def action_sold(self):
        print(" reached ".center(100, '='))
    
        # print("current user :",self.env.user)
        # print("self.env.user.has_group :",self.env.user.has_group)


        self.env['account.move'].create(
            {
                "partner_id": self.buyer_id.id,
                "move_type": 'out_invoice',
                "invoice_date": fields.Date.today(),
                "invoice_line_ids": [
                    Command.create(
                        {
                            "name": self.name,
                            "quantity": 1,
                            "price_unit": self.selling_price,
                        }),
                    Command.create(
                    {
                        "name": self.name,
                        "quantity": 2,
                        "price_unit": self.selling_price * 0.06,
                    }),
                    Command.create({

                        "name": "Administrative fees",
                        "quantity": 1,
                        "price_unit": 100.0,
                    })]
            }
        )
        return super().action_sold()
