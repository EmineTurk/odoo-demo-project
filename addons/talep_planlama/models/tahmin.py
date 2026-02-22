from odoo import models, fields

class TalepTahmin(models.Model):
    _name = 'talep.tahmin'
    _description = 'Talep Tahmin'

    name = fields.Char("Tahmin")