from odoo import models,fields 
class estate_property(models.Model):
    _name = "estate.property"
    _description = 'Property and Many more'
    _log_access=False


    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode=fields.Char("Postcode", required=True)
    date_availibilty=fields.Date("Date Availibilty", required=True)
    expected_price=fields.Float("Expected Price", required=True)
    selling_price=fields.Float("Selling Price", required=True)
    bedroom=fields.Integer("Bedroom", required=True)
    living_area=fields.Integer("Living Area", required=True)
    facades=fields.Integer("Facades")
    garage=fields.Boolean("Garage")
    garden=fields.Boolean("Garden")
    garden_area=fields.Integer("Garden area")
    garden_orientation=fields.Selection( selection=[("N","North"),("S","South"),("E","East"),("W","West")]
    ,string="Garden Orientaton")
    