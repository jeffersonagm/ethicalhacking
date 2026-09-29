#Sort a list of vulnerability dicts by a numeric 'severity' field, highest first, using sorted()

vulnerabilidades = [
    {"nombre": "SQL Injection", "severidad": 9},
    {"nombre": "Cross-Site Scripting", "severidad": 6},
    {"nombre": "Insecure Deserialization", "severidad": 8},
    {"nombre": "Broken Authentication", "severidad": 7},
]

vulnerabilidades_ordenadas = sorted(vulnerabilidades, key=lambda x: x['severidad'], reverse=True)
print(vulnerabilidades_ordenadas)