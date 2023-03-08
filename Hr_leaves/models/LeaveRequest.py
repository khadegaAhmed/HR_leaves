from odoo import models, fields, api
class LeaveRequest(models.Model):
    _name = 'leavee.request'
    _inherit ='hr.employee'
    name = fields.Char(string="Description")
    from_data = fields.Date(string='From Date')
    to_date = fields.Date(string='TO Date')
    leave_type = fields.Many2one('leave.type',string="Leave Type")
    employee_id= fields.Many2one('hr.employee',string="Employee")
    stat = fields.Selection([
        ('draft', 'Draft'),
        ('inprogress', 'Inprogress'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft')
    category_ids = fields.Many2many(
        'hr.employee.category','leaveRequest_category_rel',
        'le', 'category_id',
        string='Tags')

    def action_confirm(self):
        self.stat='inprogress'

    def action_approved(self):
        self.stat = 'approved'

    def action_rejected(self):
        self.stat = 'rejected'


