import json
import hmac
import hashlib
import datetime
import urllib.request

SECRET = b"hello-there-from-b12"
URL = "https://b12.io/apply/submission"

payload = {
    "action_run_link": "https://github.com/doubleb219/B12/actions/runs/YOUR_RUN_ID",
    "email": "domiga0219@gmail.com",
    "name": "Domingo Garcia",
    "repository_link": "https://github.com/doubleb219/B12",
    "resume_link": "https://www.linkedin.com/in/dogoga/",
    "timestamp": datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
}

# Canonical JSON: sorted keys, no whitespace
body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

signature = hmac.new(SECRET, body, hashlib.sha256).hexdigest()

req = urllib.request.Request(
    URL,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={signature}",
    },
    method="POST",
)

with urllib.request.urlopen(req) as resp:
    response_body = resp.read().decode("utf-8")
    print(response_body)
