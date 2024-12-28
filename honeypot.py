import socket
import sys
import json
import threading
from pathlib import Path

class Honeypot:
    def __init__(self, bind_ip="0.0.0.0", ports=None):
        self.binf_ip = bind_ip
        self.ports = ports or [21, 22, 80, 443]
        self.active_connections = {}
        self.log_file = LOG_DIR / f"honeypot_{datetime.datetime.now().strftime('')}"
