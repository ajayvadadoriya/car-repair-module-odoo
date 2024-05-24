from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
#---------------CLASS AND IT'S ATTRIBUTES------------------
class CarRepair(models.Model):
    _name = "car.repair"
    _description = "Car Repair Record"
    _rec_name = 'ref'

    subject_id = fields.Char(string='Subject', required=True)
    assigns = fields.Many2one('res.users',string='Assigned to', required=True)
    ref = fields.Char(string="Sequence Number", copy=False, readonly=True, default=lambda self: _('New'))
    date_of_receipt = fields.Datetime(string="Date of Receipt",required=True)
    image = fields.Image(string="Image")
    client = fields.Many2one('res.partner',string="Client",required=True)
    contact = fields.Char(string="Contact Name",required=True)
    phone = fields.Char(string='Phone', required=True)
    mobile = fields.Char(string='Mobile', required=True)
    email = fields.Char(string='Email', required=True)
    contact_no = fields.Char(string='Contact_Number', required=True)
    state = fields.Selection([
        ('received', "RECEIVED"), ('in_diagnosis', "IN DIAGNOSIS"), ('quotation_sent', "QUOTATION SENT"), ('quotation_approved', "QUOTATION APPROVED"), ('work_in_progress', "WORK IN PROGRESS"),('done', "DONE")], string="Status", default='received')
    car_ids = fields.One2many('car.diagnosis','diagnosis_id',string='Car Info')
    notes = fields.Text(string="Notes")
    service_ids = fields.One2many('car.checklist','checklist_id',string='Service Repair Checklist')
    diagnosis_count = fields.Integer(string="Diagnosis Count", compute='compute_diagnosis_count')



    def action_received(self):
        self.state = 'received'

    def action_in_diagnosis(self):
        self.state = 'in_diagnosis'

    def action_quotation_sent(self):
        self.state = 'quotation_sent'

    def action_quotation_approved(self):
        self.state = 'quotation_approved'

    def action_work_in_progress(self):
        self.state = 'work_in_progress'

    def action_done(self):
        self.state = 'done'

    @api.model_create_multi
    def create(self, vls_list):
        for vls in vls_list:
            vls['ref'] = self.env['ir.sequence'].next_by_code('car.repair.sequence')
        return super(CarRepair, self).create(vls_list)

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id,f'{rec.ref}'))
        return result

    @api.depends('diagnosis_count')
    def compute_diagnosis_count(self):
        for rec in self:
            diagnosis_count = self.env['create.car_diagnosis'].search_count([('subject_id','=',rec.id)])
            rec.diagnosis_count = diagnosis_count

    def action_open_diagnosis(self):
        return {
            'name': 'Diagnosis',
            'type': 'ir.actions.act_window',
            'res_model': 'create.car_diagnosis',
            'view_mode': 'tree,form',
            'domain': [('subject_id', '=', self.id)],
            'target': 'current'
        }