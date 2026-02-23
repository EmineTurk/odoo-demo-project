from odoo import models, fields, api

class GenelBakis(models.Model):
    _name = 'talep.genel.bakis'
    _description = 'Genel Bakış'
    _auto = False  # veritabanında tablo oluşturma, sadece view

    surec_id = fields.Integer(string='Süreç ID')
    urun = fields.Char(string='Ürün')
    kanal = fields.Char(string='Kanal')
    olusturan = fields.Many2one('res.users', string='Oluşturan Kullanıcı')
    olusturma_tarihi = fields.Date(string='Oluşturma Tarihi')
    olusturma_saati = fields.Datetime(string='Oluşturma Saati')

    def action_onayla(self):
        tahmin = self.env['talep.tahmin'].search([('surec_id', '=', self.surec_id)], limit=1)
        if tahmin:
            tahmin.write({
                'onay_ocak': tahmin.ocak,
                'onay_subat': tahmin.subat,
                'onay_mart': tahmin.mart,
                'onay_nisan': tahmin.nisan,
                'onay_mayis': tahmin.mayis,
                'onay_haziran': tahmin.haziran,
                'onay_temmuz': tahmin.temmuz,
                'onay_agustos': tahmin.agustos,
                'onay_eylul': tahmin.eylul,
                'onay_ekim': tahmin.ekim,
                'onay_aralik': tahmin.aralik,
            })
        return {'type': 'ir.actions.act_window_close'}