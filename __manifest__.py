{
    'name': 'Car Repair',
    'author': 'Destiny Solution',
    #'website': 'www.Hospital.com',
    'summary': 'Car Repair and Automotive Service Maintenance Management Odoo App',
    'sequence': -100,
    'depends': ['fleet'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/security_access.xml',
        'data/sequence.xml',
        'wizard/assign_technician.xml',
        'views/menu.xml',
        'views/car_repair.xml',
        'views/car_dignosis.xml',
        'views/create_car_diagnosis.xml',
        'views/checklist.xml',
        'report/car_repair_label.xml',
        'report/reports.xml'


    ]

}
