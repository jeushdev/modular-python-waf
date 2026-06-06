from app.waf.models.request_context import RequestContext
from app.waf.rules.sqli import SQLInjectionRule
from app.waf.rules.xss import XSSRule

class WAFEngine:
    def __init__(self):
        self._rules = [SQLInjectionRule(), XSSRule()]

    def is_malicious(self, context: RequestContext) -> bool:
        for rule in self._rules:
            if rule.evaluate(context):
                return True
        return False