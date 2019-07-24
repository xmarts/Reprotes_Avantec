# -*- coding: utf-8 -*-
from odoo import http

# class Validation(http.Controller):
#     @http.route('/validation/validation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/validation/validation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('validation.listing', {
#             'root': '/validation/validation',
#             'objects': http.request.env['validation.validation'].search([]),
#         })

#     @http.route('/validation/validation/objects/<model("validation.validation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('validation.object', {
#             'object': obj
#         })