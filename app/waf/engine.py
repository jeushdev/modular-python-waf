from app.waf.models.request_context import RequestContext
from app.waf.rules.sqli import SQLInjectionRule
from app.waf.rules.xss import XSSRule
from app.waf.exceptions import MaliciousRequestException

class WAFEngine:
    def __init__(self):
        self._rules = [SQLInjectionRule(), XSSRule()]

    def is_malicious(self, context: RequestContext) -> bool:
        for rule in self._rules:
            try:
                rule.evaluate(context)
            except MaliciousRequestException as e:
                print(f"[ENGINE BLOCK] Catching threat: {e.rulename}")
                return True

        return False