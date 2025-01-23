# -*- coding: utf-8 -*-
# from odoo import http


# class Ej2(http.Controller):
#     @http.route('/ej2/ej2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ej2/ej2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ej2.listing', {
#             'root': '/ej2/ej2',
#             'objects': http.request.env['ej2.ej2'].search([]),
#         })

#     @http.route('/ej2/ej2/objects/<model("ej2.ej2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ej2.object', {
#             'object': obj
#         })

