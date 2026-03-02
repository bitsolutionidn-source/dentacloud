import frappe
from frappe.model.document import Document

class DentaPasien(Document):
    def validate(self):
        # 1. Otomatis Uppercase Nama (Seperti LOGIKA GAS ANDA)
        if self.nama_pasien:
            self.nama_pasien = self.nama_pasien.upper()
        
        # 2. Otomatis Uppercase Alergi
        if self.alergi:
            self.alergi = self.alergi.upper()

        # 3. Validasi NIK (Jika diisi harus 16 digit)
        if self.nik and len(str(self.nik)) != 16:
            frappe.throw("NIK harus berjumlah 16 digit!")
        
        # 4. Validasi Format No HP
        if self.no_hp and not self.no_hp.startswith("'"):
            # Kita bisa tambahkan petik otomatis jika perlu, 
            # tapi di Frappe Phone field otomatis menangani formatting.
            pass
