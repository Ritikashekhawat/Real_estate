from odoo.http import request
from odoo import http


class Estate(http.Controller):

    @http.route(['/estate_details', '/estate_details/page/<int:page>'], type="http", auth='public', website=True)
    def index(self, page=0,**kw):
        domain=[('state', 'in', ('N','OR','OA'))]
        
        create_date1 = kw.get('create_date1')
        if create_date1:
            domain.append(('create_date','>=',create_date1))
        c_o=request.env['estate.property'].sudo().search_count(domain)
        pager = request.website.pager(
            url='/estate_details',
            page=page,
            total=c_o,
            step=6,
        )
        
        Property = http.request.env['estate.property'].sudo().search(domain,limit = 6, offset=pager['offset'])

        return http.request.render('real_estate.estate_id',{
                 'records' : Property,
                 'pager' : pager,
                 'create_date1' : create_date1
        })
        

    @http.route('/estate_details/<int:property_id>', type='http', auth='public', website=True)
    def property_details_page(self, property_id, **kwargs):
        print('-----------------------------------------------')
        property_data = request.env['estate.property'].browse(property_id)
        return http.request.render('real_estate.property_details_template', {'property_data': property_data})