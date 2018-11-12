# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class Partner(models.Model):
    _inherit = "res.partner"
    
    is_member = fields.Boolean('Member', default=False)
    reg_date = fields.Date('Registration Date', default=datetime.today())
    exp_date = fields.Date('Exipiration Date')
    reg_number = fields.Char('Registration Number', default='New')
    
    @api.model
    def create(self, vals):
        if vals.get('reg_number', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['reg_number'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('membership.reg.number') or _('New')
            else:
                vals['reg_number'] = self.env['ir.sequence'].next_by_code('membership.reg.number') or _('New')

        result = super(Partner, self).create(vals)
        return result
