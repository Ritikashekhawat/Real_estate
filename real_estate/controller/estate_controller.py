from odoo.http import request
from odoo import http


class Estate(http.Controller):

    @http.route('/estate_details', auth='public', website=True)
    def index(self, **post):
        domain=[('state', 'in', ('N','OR'))]
        Property = http.request.env['estate.property'].sudo().search(domain)
        return http.request.render('real_estate.estate_id',{
                 'records' : Property,
        })
        