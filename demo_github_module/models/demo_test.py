from odoo import models, fields

class DemoModel(models.Model):
    _name = 'demo.test.model'
    _description = 'Demo Model for GitHub Testing'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Active', default=True)
