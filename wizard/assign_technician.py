from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "assign.technician.wizard"
    _description = "Assign Technician Record"


    technician = fields.Many2one('res.users',string='Technician')


    def action_save_technician(self):
        active_id = self._context.get('active_id')
        update=self.env['create.car_diagnosis'].browse(active_id)
        vals={'assigns':self.technician}
        update.write(vals)
    # def action_create_appointment(self):
    #     vals = {
    #         'patient_id': self.patient_id.id,
    #         'appointment_date': self.date
    #     }
    #     self.env['hospital.appointment'].create(vals)


    # def print_report(self):
    #     data = {
    #         'model':'create.appointment.wizard',
    #         'form': self.read()[0]
    #     }
    #     if data['form']['patient_id']:
    #         select_patient =data['form']['patient_id'][0]
    #         appointment=self.env['hospital.appointment'].search([('patient_id', '=', select_patient)])
    #     else:
    #         appointment = self.env['hospital.appointment'].search([])
    #     appointment_list=[]
    #     for i in appointment:
    #         vals = {
    #             'name':i.patient_id,
    #             # 'age':i.age,
    #             # 'appointment_date':i.date
    #         }
    #         appointment_list.append(vals)
    #     data['appointment'] =appointment_list
    #     return self.env.ref('new_hospital.report_appointment').report_action(self,data=data)

    # def action_view_appointment(self):
    #     action = self.env.ref('new_hospital.action_hospital_appointment').read()[0]
    #     action['domain'] = [('patient_id', '=', self.patient_id.id)]
    #     return action
