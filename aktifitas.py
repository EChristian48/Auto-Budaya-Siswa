import enum

class PPKn(enum.Enum):
    id_mapel = 2
    berita = 25

class PAI(enum.Enum):
    id_mapel = 1
    s_tahajud = 51
    s_fardhu = 48
    s_dhuha = 50
    s_tarawih = 4
    tadarus = 5
    hafalan = 52

class PJOK(enum.Enum):
    id_mapel = 3
    olahraga_ringan = 6
    bebersih_rumah = 53
    bebersih_toilet = 54


class Aktifitas:
    def __init__(self, waktu_mulai: str = None, waktu_selesai: str = None, id_mapel: int = None,
                 id_aktifitas: int = None):
        self.waktu_mulai = waktu_mulai
        self.waktu_selesai = waktu_selesai
        self.id_mapel = str(id_mapel)
        self.id_aktifitas = str(id_aktifitas)