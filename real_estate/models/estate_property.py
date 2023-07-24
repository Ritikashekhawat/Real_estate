from odoo import models, fields
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare, float_is_zero
from odoo.exceptions import ValidationError


class estate_property(models.Model):
    _name = "estate.property"
    _inherit ='mail.thread'
    _description = 'Property and Many more'
    _log_access = False
    _order = "id desc"

    name = fields.Char("Title", required=True,traking=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode", required=True)
    date_availibilty = fields.Datetime(
        "Available From", default=lambda self: fields.Datetime.today() + relativedelta(months=3), copy=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float(
        "Selling Price", readonly=True, copy=False, default="2000")
    bedroom = fields.Integer("Bedroom", default=2)
    living_area = fields.Integer("Living Area", required=True)
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden", readonly=False)
    state = fields.Selection([('N', 'New'), ('OR', 'Offer Received'), (
        'OA', 'Offer Accepted'), ('S', 'Sold'), ('c', 'Cancelled ')], 'Status',default="N")
    garden_area = fields.Integer(
        "Garden area", compute="_compute_garden_area", readonly=False)
    garden_orientation = fields.Selection(selection=[("N", "North"), ("S", "South"), ("E", "East"), (
        "W", "West")], string="Garden Orientaton", compute="_compute_garden_area", readonly=False)
    active = fields.Boolean('Active', default=True)
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    user_id = fields.Many2one(
        "res.users", string="Salesman", default=lambda self: self.env.user ,tracking=True)
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False,tracking=True)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Float(compute="_compute_total_area")
    best_offer = fields.Float("Best Offer", compute="_compute_best_offer")

     

    _sql_constraints = [('check_expected_price', 'CHECK (expected_price > 0)', 'A property expected price must be strictly positive'),
                        ('check_selling_price', 'CHECK (selling_price > 0)', 'A property selling price must be strictly positive')]

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
                BO.best_offer = 0

    @api.depends("garden")
    def _compute_garden_area(self):
        for i in self:
            if i.garden:
                i.garden_area = 10
                i.garden_orientation = 'N'
            else:
                i.garden_area = 0
                i.garden_orientation = ''

    def action_cancel(self):
        # for i in self:
        if self.state == 'S':
            raise UserError("A sold property cannot be canceled.")
        else:
            self.state = 'c'

    def action_sold(self):
        # for i in self:
        if self.state == 'c':
            raise UserError("A canceled property cannot be sold.")
        else:
            self.state = 'S'

    @api.constrains('selling_price', 'expected_price')
    def _check_difference(self):
        for i in self:
            if (
                not float_is_zero(i.selling_price, precision_rounding=0.01)
                and float_compare(i.selling_price, i.expected_price*0.90, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price cannot be lower than 90% of the expected price.")
    
    
    @api.ondelete(at_uninstall=False)
    def _unlink_except_state(self):
        for i in self:
            if i.state not in ['N', 'c']:
                raise Warning("You can only delete properties with state 'New' or 'Canceled'.")


    def action_make_offer(self):
        return{
         'type' : "ir.actions.act_window",
         'name' : 'Add Offer',
         'res_model' : 'estate.property.wizard',
         'view_mode' : 'form',
         'target' : 'new',
    }