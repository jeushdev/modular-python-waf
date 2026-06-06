from flask import Request
import urllib.parse

class RequestContext:
    def __init__(self, request: Request):
        self._ip_address = request.remote_addr
        self._method = request.method
        self._path = request.path
        self._inputs = {}

        temp_dict = dict(request.args) | dict(request.form)
        
        for key, value in temp_dict.items():
            self._inputs[key] = urllib.parse.unquote(value)
    
    @property
    def ip_address(self) -> str:
        return self._ip_address

    @property
    def method(self) -> str:
        return self._method
    
    @property
    def path(self) -> str:
        return self._path
    
    @property
    def inputs(self) -> dict:
        return self._inputs
    
    