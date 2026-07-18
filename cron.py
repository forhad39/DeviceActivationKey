import requests
import time
from datetime import datetime, timezone
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests.exceptions import RequestException

BASE_URL = "https://jaiclub70.sbs/"
REQUEST_TIMEOUT = 15

# Create persistent session
session = requests.Session()

# Retry strategy
retries = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Fake browser headers
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
})

def log(msg):
    print(f"{datetime.now(timezone.utc).isoformat()} | {msg}")

def run(script):
    url = BASE_URL + script

    try:
        r = session.get(url, timeout=REQUEST_TIMEOUT)

        log(f"{script} | {r.status_code}")

    except RequestException as e:
        log(f"{script} | ERROR: {str(e)}")

last_30 = None
last_60 = None
last_180 = None
last_300 = None
last_600 = None

try:
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
            time.sleep(1)

        if s60 != last_60:
            scripts = [
                "niyamitakelasa.php",
                "niyamitakelasa_aidudi.php",
                "niyamitakelasa_kemuru.php",
                "ktrx.php"
            ]

            for s in scripts:
                run(s)
                time.sleep(1)

            last_60 = s60

        if s180 != last_180:
            scripts = [
                "niyamitakelasa_drei.php",
                "niyamitakelasa_aidudi_drei.php",
                "niyamitakelasa_kemuru_drei.php",
                "ktrx3.php"
            ]

            for s in scripts:
                run(s)
                time.sleep(1)

            last_180 = s180

        if s300 != last_300:
            scripts = [
                "niyamitakelasa_funf.php",
                "niyamitakelasa_aidudi_funf.php",
                "niyamitakelasa_kemuru_funf.php",
                "ktrx5.php"
            ]

            for s in scripts:
                run(s)
                time.sleep(1)

            last_300 = s300

        if s600 != last_600:
            scripts = [
                "niyamitakelasa_zehn.php",
                "niyamitakelasa_aidudi_zehn.php",
                "niyamitakelasa_kemuru_zehn.php",
                "ktrx10.php"
            ]

            for s in scripts:
                run(s)
                time.sleep(1)

            last_600 = s600

        time.sleep(0.5)

except KeyboardInterrupt:
    log("STOPPED by user")
