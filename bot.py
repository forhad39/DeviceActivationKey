import requests
import time
from datetime import datetime, timezone

BASE_URL = "https://109winclub.sbs/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def run(script):
    url = BASE_URL + script
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        print(f"{datetime.now(timezone.utc).isoformat()} | {script} | {r.status_code}")
    except Exception as e:
        print(f"{datetime.now(timezone.utc).isoformat()} | {script} | ERROR: {e}")

last_30 = last_60 = last_180 = last_300 = last_600 = None

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
            time.sleep(1)
        last_60 = s60

    if s180 != last_180:
        for x in [
            "niyamitakelasa_drei.php",
            "niyamitakelasa_aidudi_drei.php",
            "niyamitakelasa_kemuru_drei.php",
            "ktrx3.php"
        ]:
            run(x)
            time.sleep(1)
        last_180 = s180

    if s300 != last_300:
        for x in [
            "niyamitakelasa_funf.php",
            "niyamitakelasa_aidudi_funf.php",
            "niyamitakelasa_kemuru_funf.php",
            "ktrx5.php"
        ]:
            run(x)
            time.sleep(1)
        last_300 = s300

    if s600 != last_600:
        for x in [
            "niyamitakelasa_zehn.php",
            "niyamitakelasa_aidudi_zehn.php",
            "niyamitakelasa_kemuru_zehn.php",
            "ktrx10.php"
        ]:
            run(x)
            time.sleep(1)
        last_600 = s600

    time.sleep(1)
