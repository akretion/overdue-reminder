# Copyright 2020 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountInvoiceOverdueReminder(models.Model):
    _name = 'account.invoice.overdue.reminder'
    _description = 'Overdue Invoice Reminder Action History'
    _order = 'date desc, id desc'

    # For the link to invoice: why a M2O and not a M2M ?
    # Because of the "counter" field: a single reminder action for a customer,
    # the "counter" may not be the same for each invoice
    invoice_id = fields.Many2one(
        'account.invoice', string='Invoice', ondelete='cascade')
    partner_id = fields.Many2one(
        related='invoice_id.commercial_partner_id', store=True,
        string='Customer')
    date = fields.Date(default=fields.Date.context_today, required=True)
    user_id = fields.Many2one(
        'res.users', string='Performed by', required=True,
        ondelete='restrict', default=lambda self: self.env.user)
    reminder_type = fields.Selection(
        '_reminder_type_selection', default='mail', string='Type',
        required=True)
    result_id = fields.Many2one(
        'overdue.reminder.result', ondelete='restrict',
        string='Result/Info')
    result_notes = fields.Text(string='Call Notes')
    mail_id = fields.Many2one('mail.mail', string='Reminder E-mail')
    mail_state = fields.Selection(
        related='mail_id.state', string='E-mail Status')
    counter = fields.Integer()
    company_id = fields.Many2one(
        related='invoice_id.company_id', store=True)

    _sql_constraints = [(
        'counter_positive',
        'CHECK(counter >= 0)',
        'Counter must always be positive')]

    @api.model
    def _reminder_type_selection(self):
        return [
            ('mail', _('E-mail')),
            ('phone', _('Phone')),
            ('post', _('Post')),
            ]

    @api.constrains('invoice_id')
    def invoice_id_check(self):
        for action in self:
            if action.invoice_id and action.invoice_id.type != 'out_invoice':
                raise ValidationError(_(
                    "An overdue reminder can only be attached "
                    "to a customer invoice"))
