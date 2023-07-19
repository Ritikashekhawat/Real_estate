from odoo import fields,models,Command


class EstateProperty(models.Model):

    _name = 'estate.property'
    _inherit = "estate.property"

    def action_sold(self):
        print("------------project----")

        self.env['project.project'].create(
            {
                "name": "Sold Properties",
                "active": True
            }
        )
        project = self.env['project.project'].search([('name', '=', 'Sold Properties')], limit=1)
        self.env['project.task'].create(
            {
                'name': self.name,
                'project_id': project.id,
                'partner_id': self.buyer_id.id,
            }
        )
        return super().action_sold()
