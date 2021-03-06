# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Attendances',
    'version': '2.0',
    'author': "HashMicro / Selvakumar D - Ajay Patel",
    'category': 'Human Resources',
    'sequence': 81,
    'summary': 'Manage employee attendances',
    'description': """
This module aims to manage employee's attendances.
==================================================

Keeps account of the attendances of the employees on the basis of the
actions(Check in/Check out) performed by them.
       """,
    'website': 'https://www.odoo.com/page/employees',
    'depends': ['hr', 'report', 'hr_dashboard','sg_hr_employee'],
    'data': [
        'data/hr_attendance_data.xml',
        'report/emp_report.xml',
        'report/report_template.xml',
        'views/extended_hr_employee_view.xml',
        'views/res_config_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
