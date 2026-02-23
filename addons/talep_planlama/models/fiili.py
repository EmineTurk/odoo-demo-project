from odoo import models, fields, api

class TalepFiili(models.Model):
    _name = 'talep.fiili'
    _description = 'Fiili Miktar Tablosu'

    surec_id = fields.Integer(string='Süreç ID', readonly=True)
    urun = fields.Char(string='Ürün', required=True)
    kanal = fields.Char(string='Kanal', required=True)
    ocak = fields.Float(string='Ocak Fiili Miktar')
    subat = fields.Float(string='Şubat Fiili Miktar')
    mart = fields.Float(string='Mart Fiili Miktar')
    nisan = fields.Float(string='Nisan Fiili Miktar')
    mayis = fields.Float(string='Mayıs Fiili Miktar')
    haziran = fields.Float(string='Haziran Fiili Miktar')
    temmuz = fields.Float(string='Temmuz Fiili Miktar')
    agustos = fields.Float(string='Ağustos Fiili Miktar')
    eylul = fields.Float(string='Eylül Fiili Miktar')
    ekim = fields.Float(string='Ekim Fiili Miktar')
    aralik = fields.Float(string='Aralık Fiili Miktar')
    olusturan = fields.Many2one('res.users', string='Oluşturan Kullanıcı', default=lambda self: self.env.user, readonly=True)
    olusturma_tarihi = fields.Date(string='Oluşturma Tarihi', default=fields.Date.today, readonly=True)
    olusturma_saati = fields.Datetime(string='Oluşturma Saati', default=fields.Datetime.now, readonly=True)

    @api.model
    def create(self, vals):
        last = self.search([], order='surec_id desc', limit=1)
        vals['surec_id'] = (last.surec_id + 1) if last else 1
        return super().create(vals)