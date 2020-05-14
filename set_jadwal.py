import time
from datetime import timedelta, date
from aktiftas_harian import aktifitas_harian
from custom_driver import Budaya

# Mau ditambahin fitur input berapa hari
# Kasih while loop

# Mulai Selenium
with Budaya() as driver:
    driver.implicitly_wait(10)

    driver.login('11806588')

    delta = timedelta(1)

    for aktifitas in aktifitas_harian.values():
        driver.isi_jadwal(aktifitas, date.today())



    time.sleep(5)
