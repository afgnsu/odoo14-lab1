# -*- coding: utf-8 -*-
# from odoo import http


# class lab1(http.Controller):
#     @http.route('/lab1/lab1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lab1/lab1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lab1.listing', {
#             'root': '/lab1/lab1',
#             'objects': http.request.env['lab1.lab1'].search([]),
#         })

#     @http.route('/lab1/lab1/objects/<model("lab1.lab1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lab1.object', {
#             'object': obj
#         })
