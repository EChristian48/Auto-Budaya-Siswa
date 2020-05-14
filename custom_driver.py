from selenium.webdriver import Chrome
from aktifitas import Aktifitas
from selenium.webdriver.support.ui import Select
from datetime import datetime

class Budaya(Chrome):
    def fill_text_field(self, _id: str, value: str):
        elem = self.find_element_by_id(_id)
        elem.send_keys(value)
        return elem

    def click_link(self, text):
        elem = self.find_element_by_link_text(text)
        elem.click(elem)
        return elem

    def login(self, nis: str):
        self.get('https://budayasiswa.my.id/login')

        self.fill_text_field('username', nis)
        self.fill_text_field('password', nis).submit()

        self.find_element_by_link_text('Set Jadwal').click()

    def isi_jadwal(self, aktifitas: Aktifitas, date):
        formatted_date = (str(date.month), str(date.day), str(date.year))
        formatted_date = '-'.join(formatted_date)

        mapel_dd = Select(self.find_element_by_id('mapel'))
        aktifitas_dd = Select(self.find_element_by_id('aktifitas'))

        self.find_element_by_id('tanggal').send_keys(formatted_date)
        self.find_element_by_id('jam_mulai').send_keys(aktifitas.waktu_mulai)
        self.find_element_by_id('jam_akhir').send_keys(aktifitas.waktu_selesai)
        mapel_dd.select_by_value(aktifitas.id_mapel)
        aktifitas_dd.select_by_value(aktifitas.id_aktifitas)
        self.find_element_by_id('simpan').click()
