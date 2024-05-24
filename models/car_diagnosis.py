from odoo import api, fields, models, _


class CreateCarDiagnosis(models.TransientModel):
    _name = "car.diagnosis"
    _description = "Create Car Diagnosis Wizard"


    car = fields.Many2one('fleet.vehicle',string="Car",required=True)
    model = fields.Char(string="Model",required=True)
    license_id = fields.Char(string="License Plate",required=True)
    chassis_number = fields.Char(string="Chassis Number",required=True)
    fuel_type = fields.Selection([('gasoline', 'Gasoline'),('diesel','Diesel'),('electric','Electric'),('hybrid','Hybrid')], string="Fuel Type")
    car_manufacturing_year = fields.Char(string="Car Manufacturing Year",required=True)
    under_guarantee = fields.Selection([('yes', 'Yes'),('no','No')], string="Under Guarantee")
    guarantee_type = fields.Selection([('paid', 'Paid'),('free','Free')], string="Guarantee Type")
    service = fields.Char(string="Service Detail")
    damage = fields.Char(string="List of Damage",required=True)
    nature_of_service = fields.Many2one('fleet.vehicle.log.services',string="Nature of Service",required=True)
    state = fields.Selection([
        ('draft', "DRAFT"), ('in_diagnosis', "IN DIAGNOSIS"),('done', "DONE")],
        string="Status",
        default='draft')
    diagnosis_id = fields.Many2one('car.repair', string="Diagnosis")

