from odoo.http import request
from odoo import http


class Estate(http.Controller):

    @http.route('/estate_details', type="http", auth='public', website=True)
    def index(self, page=1,per_page=6,**kw):
        domain=[('state', 'in', ('N','OR','OA'))]
        c_o=request.env['estate.property'].search_count(domain)
        pager = request.website.pager(
            url='/estate_details',
            page=page,
            total=c_o,
            step=6,
            scope = 6,
        )
        Property = http.request.env['estate.property'].sudo().search(domain,limit = per_page,offset=pager['offset'])
        return http.request.render('real_estate.estate_id',{
                 'records' : Property,
                 'pager' : pager
        })
        

    @http.route('/estate/<model("estate.property"):property_id>/',type="http",auth='public',website=True)
    def index1(self,property_id,**kw):
        properties = http.request.env['estate.property'].sudo().browse(property_id)
        return http.request.render('real_estate.index1',{
            'properties': properties
        })