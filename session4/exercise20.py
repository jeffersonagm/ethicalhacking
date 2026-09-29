vulnerabilities = [
    {"title": "SQL Injection", "owasp_category": "A03:2021 - Injection"},
    {"title": "XSS", "owasp_category": "A03:2021 - Injection"},
    {"title": "Broken Access Control", "owasp_category": "A01:2021 - Broken Access Control"},
    {"title": "CSRF", "owasp_category": "A01:2021 - Broken Access Control"},
    {"title": "Weak Password", "owasp_category": "A07:2021 - Identification and Authentication Failures"}
]

counts = {}

for vulnerability in vulnerabilities:
    category = vulnerability["owasp_category"]
    
    if category not in counts:
        counts[category] = 0
    
    counts[category] += 1

print(counts)