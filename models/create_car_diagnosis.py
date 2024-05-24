from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


# ---------------CLASS AND IT'S ATTRIBUTES------------------
class CarRepair(models.Model):
    _name = "create.car_diagnosis"
    _description = "Car Repair Record"
    _rec_name = 'ref'

    subject_id = fields.Many2one('car.repair', string='Subject', required=True)
    assigns = fields.Many2one('res.users', string='Technician', required=True)
    ref = fields.Char(string="Sequence Number", copy=False, readonly=True, default=lambda self: _('New'))
    date_of_receipt = fields.Datetime(string="Date of Receipt", required=True)
    image = fields.Image(string="Image")
    client = fields.Many2one('res.partner', string="Client", required=True)
    contact = fields.Char(string="Contact Name", required=True)
    phone = fields.Char(string='Phone', required=True)
    mobile = fields.Char(string='Mobile', required=True)
    email = fields.Char(string='Email', required=True)
    contact_no = fields.Char(string='Contact_Number', required=True)
    state = fields.Selection([
        ('draft', "DRAFT"),('complete', "COMPLETE")], string="Status",
        default='draft')
    car_ids = fields.One2many('car.diagnosis', 'diagnosis_id', string='Car Info')
    notes = fields.Text(string="Notes")
    # car_repair_count = fields.Integer(string="Car Repair Count", compute='compute_car_repair_count')

    def action_draft(self):
        self.state = 'draft'


    def action_complete(self):
        self.state = 'complete'

    @api.model_create_multi
    def create(self, vls_list):
        for vls in vls_list:
            vls['ref'] = self.env['ir.sequence'].next_by_code('car.repair.sequence')
        return super(CarRepair, self).create(vls_list)

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f'{rec.ref}'))
        return result

    @api.depends('car_repair_count')
    def compute_car_repair_count(self):
        for rec in self:
            car_repair_count = self.env['car.repair'].search_count([('subject_id', '=', rec.id)])
            rec.car_repair_count = car_repair_count

    def action_open_car_repair(self):
        return {
            'name': 'Diagnosis',
            'type': 'ir.actions.act_window',
            'res_model': 'car.repair',
            'view_mode': 'tree,form',
            'domain': [('subject_id', '=', self.id)],
            'target': 'current'
        }

    def action_assign_technician(self):
        for rec in self:
            rec.env['assign.technician.wizard'].create({
                'technician': self.technician.id,
            })
