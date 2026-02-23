from odoo import models, fields, api

class TalepTahmin(models.Model):
    _name = 'talep.tahmin'
    _description = 'Tahmin Tablosu'

    surec_id = fields.Integer(string='Süreç ID', readonly=True)
    urun = fields.Char(string='Ürün', required=True)
    kanal = fields.Char(string='Kanal', required=True)
    ocak = fields.Float(string='Ocak Miktar')
    subat = fields.Float(string='Şubat Miktar')
    mart = fields.Float(string='Mart Miktar')
    nisan = fields.Float(string='Nisan Miktar')
    mayis = fields.Float(string='Mayıs Miktar')
    haziran = fields.Float(string='Haziran Miktar')
    temmuz = fields.Float(string='Temmuz Miktar')
    agustos = fields.Float(string='Ağustos Miktar')
    eylul = fields.Float(string='Eylül Miktar')
    ekim = fields.Float(string='Ekim Miktar')
    aralik = fields.Float(string='Aralık Miktar')
    olusturan = fields.Many2one('res.users', string='Oluşturan Kullanıcı', default=lambda self: self.env.user, readonly=True)
    olusturma_tarihi = fields.Date(string='Oluşturma Tarihi', default=fields.Date.today, readonly=True)
    olusturma_saati = fields.Datetime(string='Oluşturma Saati', default=fields.Datetime.now, readonly=True)
    onay_ocak = fields.Float(string='Onay Ocak')
    onay_subat = fields.Float(string='Onay Şubat')
    onay_mart = fields.Float(string='Onay Mart')
    onay_nisan = fields.Float(string='Onay Nisan')
    onay_mayis = fields.Float(string='Onay Mayıs')
    onay_haziran = fields.Float(string='Onay Haziran')
    onay_temmuz = fields.Float(string='Onay Temmuz')
    onay_agustos = fields.Float(string='Onay Ağustos')
    onay_eylul = fields.Float(string='Onay Eylül')
    onay_ekim = fields.Float(string='Onay Ekim')
    onay_aralik = fields.Float(string='Onay Aralık')

    fiili_ocak = fields.Float(string='Fiili Ocak', compute='_compute_fiili', store=False)
    fiili_subat = fields.Float(string='Fiili Şubat', compute='_compute_fiili', store=False)
    fiili_mart = fields.Float(string='Fiili Mart', compute='_compute_fiili', store=False)
    fiili_nisan = fields.Float(string='Fiili Nisan', compute='_compute_fiili', store=False)
    fiili_mayis = fields.Float(string='Fiili Mayıs', compute='_compute_fiili', store=False)
    fiili_haziran = fields.Float(string='Fiili Haziran', compute='_compute_fiili', store=False)
    fiili_temmuz = fields.Float(string='Fiili Temmuz', compute='_compute_fiili', store=False)
    fiili_agustos = fields.Float(string='Fiili Ağustos', compute='_compute_fiili', store=False)
    fiili_eylul = fields.Float(string='Fiili Eylül', compute='_compute_fiili', store=False)
    fiili_ekim = fields.Float(string='Fiili Ekim', compute='_compute_fiili', store=False)
    fiili_aralik = fields.Float(string='Fiili Aralık', compute='_compute_fiili', store=False)

    @api.depends('surec_id')
    def _compute_fiili(self):
        for rec in self:
            fiili = self.env['talep.fiili'].search([('surec_id', '=', rec.surec_id)], limit=1)
            rec.fiili_ocak = fiili.ocak if fiili else 0
            rec.fiili_subat = fiili.subat if fiili else 0
            rec.fiili_mart = fiili.mart if fiili else 0
            rec.fiili_nisan = fiili.nisan if fiili else 0
            rec.fiili_mayis = fiili.mayis if fiili else 0
            rec.fiili_haziran = fiili.haziran if fiili else 0
            rec.fiili_temmuz = fiili.temmuz if fiili else 0
            rec.fiili_agustos = fiili.agustos if fiili else 0
            rec.fiili_eylul = fiili.eylul if fiili else 0
            rec.fiili_ekim = fiili.ekim if fiili else 0
            rec.fiili_aralik = fiili.aralik if fiili else 0

    @api.model
    def create(self, vals):
        last = self.search([], order='surec_id desc', limit=1)
        vals['surec_id'] = (last.surec_id + 1) if last else 1
        return super().create(vals)

    def action_onayla(self):
        self.write({
            'onay_ocak': self.ocak,
            'onay_subat': self.subat,
            'onay_mart': self.mart,
            'onay_nisan': self.nisan,
            'onay_mayis': self.mayis,
            'onay_haziran': self.haziran,
            'onay_temmuz': self.temmuz,
            'onay_agustos': self.agustos,
            'onay_eylul': self.eylul,
            'onay_ekim': self.ekim,
            'onay_aralik': self.aralik,
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': 'İşlem yapılmıştır.',
                'type': 'success',
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }