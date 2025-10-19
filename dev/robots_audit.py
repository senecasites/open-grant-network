import requests, csv, datetime
from urllib.parse import urljoin

def check_robots(domain):
    url = urljoin(f"https://{domain}", "/robots.txt")
    try:
        r = requests.get(url, timeout=10)
        allowed = 1 if "Disallow: /" not in r.text else 0
        delay = next((line.split(":")[1].strip() for line in r.text.splitlines() if "Crawl-delay" in line), "N/A")
        return [domain, allowed, delay, datetime.datetime.now()]
    except Exception:
        return [domain, 0, "Error", datetime.datetime.now()]

with open("allow_list_policy.csv") as f, open("robots_audit_log.csv", "w", newline="") as out:
    reader, writer = csv.reader(f), csv.writer(out)
    writer.writerow(["domain", "robots_allowed", "crawl_delay", "last_checked"])
    for row in reader:
        writer.writerow(check_robots(row[0]))
