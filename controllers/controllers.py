# -*- coding: utf-8 -*-
from odoo import http

# class BoomBoomApp(http.Controller):
#     @http.route('/boom_boom_app/boom_boom_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/boom_boom_app/boom_boom_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('boom_boom_app.listing', {
#             'root': '/boom_boom_app/boom_boom_app',
#             'objects': http.request.env['boom_boom_app.boom_boom_app'].search([]),
#         })

#     @http.route('/boom_boom_app/boom_boom_app/objects/<model("boom_boom_app.boom_boom_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('boom_boom_app.object', {
#             'object': obj
#         })