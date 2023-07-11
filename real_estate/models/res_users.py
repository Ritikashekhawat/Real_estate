from odoo import models, fields

class res_users(models.Model):
    _name = "res.users"
    _description = 'Res Users'
    _inherit = "res.users"


    property_ids= fields.One2many("estate.property","user_id",string="Res Users",domain="[('state', 'in', ('N','OR'))]")

