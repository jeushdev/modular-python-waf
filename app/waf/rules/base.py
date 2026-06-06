from app.waf.models.request_context import RequestContext
from abc import ABC, abstractmethod

class BaseRule(ABC):
    def __init__(self, name, severity):
        self._name = name
        self._severity = severity

    @abstractmethod
    def evaluate(self, context: RequestContext) -> bool:
        pass    

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def severity(self) -> str:
        return self._severity