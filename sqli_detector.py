import requests

def detect_sql_injection(url, param, payloads):
    vulnerable = False
    for payload in payloads:
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)
        if "SQL syntax" in response.text or "sql error" in response.text:
            print(f"Possible SQL Injection vulnerability detected with payload: {payload}")
            vulnerable = True
            break
    return vulnerable

if __name__ == "__main__":
    url = "http://example.com/vulnerable_endpoint"
    param = "id"
    payloads = ["1 UNION SELECT null--", "1' UNION SELECT null--", "' OR '1'='1'--"]
    if detect_sql_injection(url, param, payloads):
        print("SQL Injection vulnerability detected!")
    else:
        print("No vulnerabilities detected.")
