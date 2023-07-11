
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

from odoo.tools.float_utils import float_compare


class estate_property_offer(models.Model):

    _name = "estate.property.offer"
    _description = 'Property offer'
   # _log_access=False

    price = fields.Float("price", required=True)
    status = fields.Selection(selection=[(
        "A", "Accepted"), ("R", "Refused"),], string="Status", copy=False)
    partner_id = fields.Many2one(
        "res.partner", string="partner", required=True)
    property_id = fields.Many2one(
        "estate.property", string="property", required=True)
    Validity = fields.Integer("Validity", default=7)
    date_deadline = fields.Date(
        compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    _order = "price desc"

    property_type_id = fields.Many2one("estate.property.type",related="property_id.property_type_id" ,store=True)
    
    _sql_constraints = [('check_price', 'CHECK (price > 0)',
                         'An offer price must be strictly positive')]

    @api.depends('Validity')
    def _compute_date_deadline(self):
        for record in self:
            if type(record.create_date) is not bool:
                record.date_deadline = fields.Date.add(
                    record.create_date, days=record.Validity)
            else:
                record.date_deadline = fields.Date.add(
                    fields.Datetime.today(), days=record.Validity)

    def _inverse_date_deadline(self):
        for record in self:
            print("self", self)
            if type(record.create_date) is not bool:
                record.Validity = (record.date_deadline -
                                   record.create_date.date()).days
            else:
                record.Validity = (record.date_deadline -
                                   fields.Datetime.today().date()).days

    def action_accept(self):
        for i in self:
            i.status = "A"
            i.property_id.selling_price = i.price
            i.property_id.buyer_id = i.partner_id
            i.property_id.state = "OA"

    def action_refuse(self):
        for i in self:
            i.status = "R"
            i.property_id.selling_price = 0
   

    def action_view(self):
        for i in self:
            i.status = "R"
            i.property_id.selling_price = 0
   

    @api.model
    def create(self, vals):
        if vals.get("property_id") and vals.get("price"):
            property_id = self.env["estate.property"].browse(vals["property_id"])
            if property_id.offer_ids:
                max_offer = max(property_id.mapped("offer_ids.price"))
                if float_compare(vals["price"], max_offer, precision_rounding=0.01) <= 0:
                    raise UserError("The offer must be higher than %.2f" % max_offer)
            property_id.state = "OR"
        return super().create(vals)

