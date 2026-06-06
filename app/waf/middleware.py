from app.waf.models.request_context import RequestContext
from app.waf.engine import WAFEngine
from flask import Flask, request, abort
from app.waf.exceptions import MaliciousRequestException

app = Flask(__name__)

class WAFMiddleware:
    def __init__(self, app):
        app.before_request(self.intercept)
        self._engine = WAFEngine()
    
    def intercept(self):
        context = RequestContext(request)
        try:
            if self._engine.is_malicious(context):
                abort(403)
        except MaliciousRequestException as e:
            print(f"\n[PERIMETER ALERT] !!! INTRUSION ATTEMPT BLOCKED !!!")
            print(f"-> TRIGGERED BY: {e.rulename}")
            print(f"-> SEVERITY:     {e.severity}")
            print(f"-> OFFENDING RAW PAYLOAD: {e.payload}")
            print(f"-> TARGET ENDPOINT:       {request.path}\n")
            abort(403)
            