from aktifitas import Aktifitas, PAI, PJOK, PPKn

aktifitas_harian = {
    'shalat_tahajud': Aktifitas('03:00', '03:15', PAI.id_mapel.value, PAI.s_tahajud.value),
    'shalat_subuh': Aktifitas('05:00', '05:15', PAI.id_mapel.value, PAI.s_fardhu.value),
    'shalat_dhuha': Aktifitas('07:20', '07:30', PAI.id_mapel.value, PAI.s_dhuha.value),
    'olahraga_ringan': Aktifitas('07:30', '07:40', PJOK.id_mapel.value, PJOK.olahraga_ringan.value),
    'berita': Aktifitas('13:00', '14:00', PPKn.id_mapel.value, PPKn.berita.value),
    'shalat_dzuhur': Aktifitas('11:55', '12:10', PAI.id_mapel.value, PAI.s_fardhu.value),
    'tadarus': Aktifitas('12:10', '12:20', PAI.id_mapel.value, PAI.tadarus.value),
    'hafalan': Aktifitas('12:20', '12:30', PAI.id_mapel.value, PAI.hafalan.value),
    'shalat_ashar': Aktifitas('15:20', '15:30', PAI.id_mapel.value, PAI.s_fardhu.value),
    'shalat_maghrib': Aktifitas('17:50', '18:15', PAI.id_mapel.value, PAI.s_fardhu.value),
    'shalat_isya': Aktifitas('19:00', '19:15', PAI.id_mapel.value, PAI.s_fardhu.value),
    'shalat_tarawih': Aktifitas('19:15', '19:45', PAI.id_mapel.value, PAI.s_tarawih.value),
}