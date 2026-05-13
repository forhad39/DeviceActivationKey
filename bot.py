import requests
import time
from datetime import datetime, timezone

BASE_URL = "https://109winclub.sbs/"

session = requests.Session()

def run(script):
    url = BASE_URL + script

    try:
        r = session.get(url, timeout=15)

        if r.status_code == 200:
            print(f"{datetime.now(timezone.utc).isoformat()} | {script} | OK")
        elif r.status_code == 404:
            print(f"{datetime.now(timezone.utc).isoformat()} | {script} | FILE NOT FOUND")
        elif r.status_code == 500:
            print(f"{datetime.now(timezone.utc).isoformat()} | {script} | SERVER ERROR")
        else:
            print(f"{datetime.now(timezone.utc).isoformat()} | {script} | STATUS {r.status_code}")

    except requests.exceptions.Timeout:
        print(f"{datetime.now(timezone.utc).isoformat()} | {script} | TIMEOUT")

    except requests.exceptions.RequestException as e:
        print(f"{datetime.now(timezone.utc).isoformat()} | {script} | ERROR: {e}")


last_30 = None
last_60 = None
last_180 = None
last_300 = None
last_600 = None

while True:
    now = time.time()

    s30 = int(now // 30)
    s60 = int(now // 60)
    s180 = int(now // 180)
    s300 = int(now // 300)
    s600 = int(now // 600)

    if s30 != last_30:
        run("niyamitakelasa30sec.php")
        last_30 = s30

    if s60 != last_60:
        for x in [
            "niyamitakelasa.php",
            "niyamitakelasa_aidudi.php",
            "niyamitakelasa_kemuru.php",
            "ktrx.php"
        ]:
            run(x)

        last_60 = s60

    if s180 != last_180:
        for x in [
            "niyamitakelasa_drei.php",
            "niyamitakelasa_aidudi_drei.php",
            "niyamitakelasa_kemuru_drei.php",
            "ktrx3.php"
        ]:
            run(x)

        last_180 = s180

    if s300 != last_300:
        for x in [
            "niyamitakelasa_funf.php",
            "niyamitakelasa_aidudi_funf.php",
            "niyamitakelasa_kemuru_funf.php",
            "ktrx5.php"
        ]:
            run(x)

        last_300 = s300

    if s600 != last_600:
        for x in [
            "niyamitakelasa_zehn.php",
            "niyamitakelasa_aidudi_zehn.php",
            "niyamitakelasa_kemuru_zehn.php",
            "ktrx10.php"
        ]:
            run(x)

        last_600 = s600

    time.sleep(1)
