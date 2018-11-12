# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Company(models.Model):
    _inherit = "res.company"
    
    membership_active_day = fields.Integer('Membership Active Days', default=30)
