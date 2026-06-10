from datetime import datetime

class WAFTelemetry():
    def __init__(self):
        self.logs = []
    
    def record_attack(self, rulename: str, severity: str, payload: str, path: str):
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "rulename": rulename,
            "severity": severity,
            "payload": payload,
            "path": path
        }

        self.logs.append(log_entry)

# The central telemetry warehouse instance
telemetry_warehouse = WAFTelemetry()