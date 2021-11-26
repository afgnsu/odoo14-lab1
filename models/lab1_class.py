# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError


class Lab1Class(models.Model):
    _name = 'lab1.class'

    class_name = fields.Char(string='班級')
    class_teacher = fields.Many2one('lab1.teacher', string='班導')
    class_line = fields.One2many('lab1.student', 'student_id', string='學員明細')

    #@api.multi
    def name_get(self):
        result = []
        for rec in self:
            myname = '[%s]%s' % (rec.class_name, rec.class_teacher.teacher_name)
            result.append((rec.id, myname))
        return result