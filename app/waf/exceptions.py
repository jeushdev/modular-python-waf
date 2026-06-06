class MaliciousRequestException(Exception):
    def __init__(self, rulename, severity, payload):
        super().__init__(f"WAF Blocked a {severity} threat triggered by {rulename}") 
        self._rulename = rulename
        self._severity = severity
        self._payload = payload

    @property
    def rulename(self) -> str:
        return self._rulename

    @property
    def severity(self) -> str:
        return self._severity

    @property
    def payload(self) -> str:
        return self._payload