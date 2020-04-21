# Copyright 2020 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Overdue Invoice Reminder',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': 'Simple mail/letter/phone overdue customer invoice reminder ',
    'author': 'Akretion',
    'maintainers': ['alexis-via'],
    'website': 'http://www.akretion.com',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'security/rule.xml',
        'views/partner.xml',
        'views/report.xml',
        'views/report_overdue_reminder.xml',
        'views/account_invoice.xml',
        'views/account_invoice_overdue_reminder.xml',
        'views/overdue_reminder_result.xml',
        'views/config_settings.xml',
        'wizard/overdue_reminder_wizard_view.xml',
        'data/overdue_reminder_result.xml',
        'data/mail_template.xml',
    ],
    'installable': True,
    'application': True,
}
