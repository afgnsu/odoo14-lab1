# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime


class Lab1Student(models.Model):
    _name = 'lab1.student'

    student_id = fields.Many2one('lab1.class', ondelete='cascade')
    student_no = fields.Char(string='學生學號', required=True)
    student_name = fields.Char(string='學生姓名', required=True)
    student_contact = fields.Char(string='聯絡人')
    student_class = fields.Selection([('1', '一年級'), ('2', '二年級'), ('3', '三年級')], string='年級')
    student_birthday = fields.Date(string='生日', default=datetime.now().strftime('%Y-%m-%d'))
    student_fm = fields.Selection([('M', '男'), ('F', '女')], string='性別', default='M')
    student_memo = fields.Text(string='備註')
    student_obj = fields.Html(string='圖片')

    #@api.multi
    def name_get(self):
        result = []
        for rec in self:
            if rec.student_class == '1':
                myclass = '一年級'
            elif rec.student_class == '2':
                myclass = '二年級'
            elif rec.student_class == '3':
                myclass = '三年級'
            myname = '[%s]%s-%s' % (rec.student_no, rec.student_name, myclass)
            result.append((rec.id, myname))
        return result