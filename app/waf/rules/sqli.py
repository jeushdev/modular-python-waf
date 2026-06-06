from app.waf.rules.base import BaseRule
from app.waf.models.request_context import RequestContext
from app.waf.exceptions import MaliciousRequestException
import re

class SQLInjectionRule(BaseRule):
    def __init__(self):
        super().__init__("SQL Injection Engine", "CRITICAL")
    
    def evaluate(self, context: RequestContext) -> bool:
        sqli_pattern = r"('|\b)(or|and)\b\s+\d+=\d+|'|--|\bunion\b|\bselect\b"
        for value in context.inputs.values():
            if re.search(sqli_pattern, value, re.IGNORECASE):
                raise MaliciousRequestException(
                    rulename=self.name,
                    severity=self.severity,
                    payload=value
                )
        return False
