from app.waf.models.request_context import RequestContext
from app.waf.engine import WAFEngine
from flask import Flask, request, abort

app = Flask(__name__)

class WAFMiddleware:
    def __init__(self, app):
        app.before_request(self.intercept)
        self._engine = WAFEngine()
    
    def intercept(self):
        context = RequestContext(request)
        if self._engine.is_malicious(context):
            abort(403)
            