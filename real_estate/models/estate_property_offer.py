
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class estate_property_offer(models.Model):

    _name = "estate.property.offer"
    _description = 'Property offer'
    _log_access=False

    price = fields.Float("price",required=True)
    status = fields.Selection(selection=[("a", "Accepted"),("r", "Refused"),],string="Status",copy=False,default='A')
    partner_id = fields.Many2one("res.partner",string="partner",required=True)
    property_id = fields.Many2one("estate.property",string="property",required=True)
    Validity = fields.Integer("Validity",default=7)
    date_deadline=fields.Datetime("Deadline")


    @api.depends("create_date","Validity")
    def _compute_date_deadline(self):
        for DD in self:
            if DD.create_date:
             date = DD.create_date.date()
            else:
               date= fields.Date.today()
               DD.date_deadline = DD.date + relativedelta(days=DD.Validity)


    def _inverse_date_deadline(self):
        for DD in self:
            if DD.create_date :
             date = DD.create_date.date() 
            else:
               date=fields.Date.today()
               DD.Validity = (DD.date_deadline - date).days




