# -*- coding: utf-8 -*-
# from odoo import http


# class CallCenter(http.Controller):
#     @http.route('/call_center/call_center/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/call_center/call_center/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('call_center.listing', {
#             'root': '/call_center/call_center',
#             'objects': http.request.env['call_center.call_center'].search([]),
#         })

#     @http.route('/call_center/call_center/objects/<model("call_center.call_center"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('call_center.object', {
#             'object': obj
#         })
