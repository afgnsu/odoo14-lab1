# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError


class Lab1Score(models.Model):
    _name = "lab1.score"

    score_year = fields.Char(string='學年', required=True)
    score_student = fields.Many2one('lab1.student', string='學生')
    # digits = (5,1)，5代表包含小數點共5個字元，1代表小數點後的位數
    score_chinese = fields.Float(string='國文分數', default=0, digits=(5, 1))
    score_math = fields.Float(string='數學分數', default=0, digits=(5, 1))
    score_english = fields.Float(string='英文分數', default=0, digits=(5, 1))
    # compute代表計算而來的，並不會在資料庫產生欄位、儲存資料
    score_total = fields.Float(string='總分', compute='_get_tot')
    score_avg = fields.Float(string='平均', compute='_get_avg')
    score_bank = fields.Many2one('res.bank', string='銀行')

    #@api.multi
    def name_get(self):
        result = []
        for rec in self:
            myname = '[%s] %s-%s' % (
            rec.score_year, rec.score_student.student_no, rec.score_student.student_name)
            result.append((rec.id, myname))
        return result

    # 必填欄位使用此方法驗證，是在UI做限制，而必填欄位使用required = True驗證，除了在UI亦在DB做限制
    @api.model
    def create(self, vals):
        if vals['score_chinese'] < 0 or vals['score_math'] < 0 or vals['score_english'] < 0:
            raise UserError('成績不能是負數')
        result = super(Lab1Score, self).create(vals)
        return result

    #@api.multi
    def write(self, vals):
        if vals['score_chinese'] < 0 or vals['score_math'] < 0 or vals['score_english'] < 0:
            raise UserError('成績不能是負數')
        result = super(Lab1Score, self).write(vals)
        return result

    #@api.multi
    def unlink(self):
        for rec in self:
            if rec.score_chinese > 0 or rec.score_math > 0 or rec.score_english > 0:
                raise UserError('已有成績，不得刪除')
        res = super(Lab1Score, self).unlink()
        return res

    @api.depends('score_chinese', 'score_math', 'score_english')
    def _get_tot(self):
        for rec in self:
            rec.update({'score_total': rec.score_chinese + rec.score_math + rec.score_english})

    @api.depends('score_chinese', 'score_math', 'score_english')
    def _get_avg(self):
        for rec in self:
            rec.update({'score_avg': (rec.score_chinese + rec.score_math + rec.score_english) / 3})