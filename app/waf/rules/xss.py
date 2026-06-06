from app.waf.rules.base import BaseRule
from app.waf.models.request_context import RequestContext
from abc import ABC, abstractmethod
import re

class XSSRule(BaseRule):
    def __init__(self):
        super().__init__("Cross-Site Scripting Engine", "CRITICAL")
    
    def evaluate(self, context: RequestContext) -> bool:
        xss_pattern = r"<script.*?>|<\/script>|javascript:|onerror=|onload=|html|<body>|<iframe"
        for value in context.inputs.values():
            if re.search(xss_pattern, value, re.IGNORECASE):
                return True
        return False
