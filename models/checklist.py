from odoo import api, fields, models, _

class CarRepair(models.Model):
    _name = "car.checklist"
    _description = "Car Checklist Record"

    name = fields.Char(string='Checklist Name', required=True)
    des = fields.Text(string='Description', required=True)
    done = fields.Boolean(string='Done',required=True)

    checklist_id = fields.Many2one('car.repair',string='service repair checklist')