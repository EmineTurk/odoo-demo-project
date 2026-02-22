from odoo import models, fields

class TalepFiili(models.Model):
    _name = 'talep.fiili'
    _description = 'Talep Fiili'

    name = fields.Char("Fiili")
    ocak = fields.Float("Ocak")
    subat = fields.Float("Şubat")