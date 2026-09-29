class Vulnerability:
    def __init__(self, title, owasp_category, severity):
        self.title = title
        self.owasp_category = owasp_category
        self.severity = severity

    def summary(self):
        return f"Title: {self.title}\nOWASP Category: {self.owasp_category}\nSeverity: {self.severity}"


vulnerability = Vulnerability(
    "SQL Injection",
    "A03:2021 - Injection",
    "High"
)

print(vulnerability.summary())