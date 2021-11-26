# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError


class Lab1Teacher(models.Model):
    _name = 'lab1.teacher'

    teacher_no = fields.Char(string='教職編號')
    teacher_name = fields.Char(string='教員姓名')

    #@api.multi
    def name_get(self):
        result = []
        for rec in self:
            myname = "[%s]%s" % (rec.teacher_no, rec.teacher_name)
            result.append((rec.id, myname))
        return result