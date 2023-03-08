from odoo import models, fields, api
class LeaveType(models.Model):
    _name = 'leave.type'
    name=fields.Char(string="Leave Type")
