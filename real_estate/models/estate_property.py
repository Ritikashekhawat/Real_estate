from odoo import models,fields 
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError



class estate_property(models.Model):
    _name = "estate.property"
    _description = 'Property and Many more'
    _log_access=False

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode=fields.Char("Postcode", required=True)
    date_availibilty=fields.Datetime("Available From",default=lambda self: fields.Datetime.today() + relativedelta(months=3),copy=False)
    expected_price=fields.Float("Expected Price", required=True)
    selling_price=fields.Float("Selling Price", readonly=True,copy=False,default="2000")
    bedroom=fields.Integer("Bedroom", default=2)
    living_area=fields.Integer("Living Area", required=True)
    facades=fields.Integer("Facades")
    garage=fields.Boolean("Garage")
    garden=fields.Boolean("Garden",readonly=False)
    state = fields.Selection([('N', 'New'),('OR', 'Offer Received'),('OA', 'Offer Accepted'),('S','Sold'),('c','Cancelled ')], 'State')
    garden_area=fields.Integer("Garden area",compute="_compute_garden_area",readonly=False)
    garden_orientation=fields.Selection( selection=[("N","North"),("S","South"),("E","East"),("W","West")],string="Garden Orientaton",compute="_compute_garden_area",readonly=False)
    active = fields.Boolean('Active', default=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids=fields.One2many('estate.property.offer','property_id')
    total_area=fields.Float(compute="_compute_total_area")
    best_offer=fields.Float("Best Offer",compute="_compute_best_offer")


    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for total in self:
            total.total_area = total.living_area + total.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for BO in self:
            if BO.offer_ids:
                BO.best_offer = max(BO.offer_ids.mapped('price'))
            else:
                BO.best_offer=0
    
    @api.depends("garden")
    def _compute_garden_area(self):
        for i in self:
            if i.garden:
                i.garden_area=10
                i.garden_orientation='N'    
            else:
                i.garden_area=0
                i.garden_orientation=''

    def action_sold(self):
        if "c" in self.mapped("state"):
             raise UserError("Canceled properties cannot be sold")
        return self.write({"state": "S"})

    def action_cancel(self):
        if "sold" in self.mapped("state"):
             raise UserError("Sold properties cannot be canceled.")
        return self.write({"state": "c"})
