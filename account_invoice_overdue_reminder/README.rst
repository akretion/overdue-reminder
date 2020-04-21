========================
Invoice Overdue Reminder
========================

.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge2|

This Odoo module is designed to send overdue invoice reminders to customers. It handles reminders by e-mail, letter and phone.

Why yet another module for invoice reminders ? Because this one is better! It has been designed from the start with the following priorities:

* **keep control**: you must keep tight control on the overdue invoice reminders that you send. Overdue invoice reminders are part of the communication with your customers, and this is very important to keep a good relation with your customers.
* **usability**: the module is easy to configure and easy to use.
* **no accounting skills needed**: the module can be used by users without accounting skills. It can even be used by salesman!
* **simplicity**: for the developers, the code is small and easy to understand.
* **multi-currency**: if you invoice your customer in another currency that your company currency, the invoice reminders only mention the currency of the invoices. And if you invoice a customer with different currencies, the reminder is clear and easy-to-understand by your customer, with a total residual per currency.

The specifications written before starting the development of this module are written in this `document <https://docs.google.com/document/d/1JIIAP5QsItbJ1zLiaGHuR0RAQplEGv3diOl-d4mS__I/edit?usp=sharing>`_ (in French).

The module has one important limitation: it sends a reminder for an invoice when it has past it's *Due Date* (which is in fact the *Final Due Date*): if the invoice has a payment term with several lines, it won't send a reminder before the last term is overdue.

An overdue reminder for a customer always include all the overdue invoices of that customer.

The module supports a clever per-invoice reminder counter mechanism:

* the reminder counter is a property of an invoice,
* the reminder counter of each overdue invoice is incremented when sending a reminder by email or by post. It is not incremented for reminders by phone.
* in an email or a letter, the subject will be *Overdue invoice reminder n°N* where N is the maximum value of the counter of the overdue invoices plus one.

There are two user interfaces to send reminders:

* the **one-by-one** interface, which displays one screen for each customer that has overdue invoices, one after the other. You should use this interface when you have a small volume of reminders to send (less an 100 overdue reminders for example). It gives you a tight control on the reminders and the possibility to easily and rapidly customize the reminder e-mails.
* the **mass** interface, which displays a list view of all customers that have overdue invoices, and you can process several reminders at the same time (via the *Actions* menu).

Configuration
=============

You should increase the **osv_memory_age_limit** (default value = 1, which means 1 hour) in the Odoo server config file: for example, you can set it to 12 (12 hours). The value must be superior to the duration of the invoicing reminder wizard from the start screen to the end.

Go to the menu *Invoicing > Configuration > Settings* then go to the section *Overdue Invoice Reminder*: you will be able to configure if you want to attach the overdue invoice to the reminder emails and set default values for some parameters.

Then, go to the menu *Settings > Technical > E-mail > Templates* and search for the mail template *Overdue Invoice Reminder*. You can edit the subject and the body of this email template. If you are in a multi-lang setup, don't forget to also update the translations.

Go to the menu *Invoicing > Configuration > Invoice Reminder Results* and customize the list of entries.

If prefer `py3o <https://github.com/OCA/reporting-engine/tree/12.0/report_py3o>`_ as reporting engine, you can use the sample py3o report for the overdue reminder letter available in the module `account_invoice_overdue_reminder_py3o <https://github.com/akretion/odoo-py3o-report-templates/tree/12.0/account_invoice_overdue_reminder_py3o>`_.

Usage
=====

Of course, before sending invoice reminders, you must import your bank statements and process them, so that you are up-to-date on customer payments.

Then, go to the menu *Invoicing > Accounting > Actions > Overdue Invoice Remind*: you will get the start screen where you can:

* filter the customers that you want to remind (filter by customer or by salesman),
* check that your bank journals are up-to-date,
* choose between the *one-by-one* and *mass* interfaces,
* customize some parameters.

Then follow the process until the end.

You can also start the invoice reminder wizard via the button *Overdue Reminder* on an overdue invoice.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/akretion/overdue-reminder>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/akretion/overdue-reminder/issues/new?body=module:%20account_invoice_overdue_reminder%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Authors
~~~~~~~

* `Akretion <https://akretion.com/>`_

Contributors
~~~~~~~~~~~~

* Alexis de Lattre <alexis.delattre@akretion.com>
