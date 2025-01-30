import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-akretion-overdue-reminder",
    description="Meta package for akretion-overdue-reminder Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_invoice_overdue_reminder',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
