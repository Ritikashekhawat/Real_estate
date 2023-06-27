from odoo import models,fields 
from dateutil.relativedelta import relativedelta
class estate_property(models.Model):
    _name = "estate.property"
    _description = 'Property and Many more'
    _log_access=False

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode=fields.Char("Postcode", required=True)
    date_availibilty=fields.Datetime("Data Availability",default=lambda self: fields.Datetime.today() + relativedelta(months=3),copy=False)
    expected_price=fields.Float("Expected Price", required=True)
    selling_price=fields.Float("Selling Price", readonly=True,copy=False,default="2000")
    bedroom=fields.Integer("Bedroom", default=2)
    living_area=fields.Integer("Living Area", required=True)
    facades=fields.Integer("Facades")
    garage=fields.Boolean("Garage")
    garden=fields.Boolean("Garden")
    state = fields.Selection([('N', 'New'),('OR', 'Offer Received'),('OA', 'Offer Accepted'),('S','Sold'),('c','Cancelled ')], 'State')
    garden_area=fields.Integer("Garden area")
    garden_orientation=fields.Selection( selection=[("N","North"),("S","South"),("E","East"),("W","West")],string="Garden Orientaton")
    active = fields.Boolean('Active', default=True)
