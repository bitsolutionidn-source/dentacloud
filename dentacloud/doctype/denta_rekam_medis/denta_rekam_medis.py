import frappe
from frappe.model.document import Document

class DentaRekamMedis(Document):
    def validate(self):
        # 1. Hitung Total Bayar
        harga = self.harga or 0
        biaya_layanan = self.biaya_layanan or 0
        self.total_bayar = harga + biaya_layanan

        # 2. Hitung Fee Dokter (Misal: persentase dari Harga Tindakan saja)
        if self.fee_drg_persen:
            self.fee_drg_amount = (self.fee_drg_persen / 100) * harga
        
        # 3. Logika Uppercase pada Tindakan (Agar standar seperti GAS)
        if self.tindakan:
            self.tindakan = self.tindakan.upper()
        
    def on_submit(self):
        # Contoh: Setelah Rekam Medis di-submit (Selesai), 
        # otomatis ubah status Pendaftaran menjadi 'Completed'
        if self.pendaftaran:
            frappe.db.set_value("Denta Pendaftaran", self.pendaftaran, "status", "Completed")
