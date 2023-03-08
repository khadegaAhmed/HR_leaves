from odoo import models, fields, api
class EmployeeRequest(models.Model):
    # _name = 'leavee.request'
    _inherit ='hr.employee'
    request_ids = fields.One2many('leavee.request','employee_id')
    request_count=fields.Integer(string="Request_count",compute='_compute_request',store=True)
    def _compute_request(self):
        for rec in self:
            rec.request_count = len(rec.request_ids)
            # request_count=self.env['leavee.request'].search_count([('employee.id' ,'=' ,rec.id)])

    def action_open_request(self):
        return {
            'name': ('Request'),
            'domain':[('employee_id','=',self.id)],
            'view_type':'form',
            'res_model':'leavee.request',
            'view_id':False,
            'view_mode':'tree,form',
            'type':'ir.actions.act_window',

        }