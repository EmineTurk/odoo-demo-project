from odoo import models, fields

class Talep(models.Model):
    _name = "talep.plan"
    _description = "Talep Plan"

    name = fields.Char(string="Talep Adı")
    description = fields.Text(string="Açıklama")
    stage = fields.Selection([
        ('draft', 'Taslak'),
        ('done', 'Tamamlandı'),
    ], string="Aşama", default='draft')