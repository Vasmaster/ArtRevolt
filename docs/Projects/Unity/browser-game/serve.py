#!/usr/bin/env python3
"""
Local web server for Unity WebGL Brotli/GZip builds.
Run from the Build folder:  python serve.py
Then open:  http://localhost:8080
"""

import http.server
import socketserver
import os

PORT = 8080

BROTLI_TYPES = {
    ".js":   "application/javascript",
    ".wasm": "application/wasm",
    ".data": "application/octet-stream",
    ".symbols.json": "application/json",
}

GZIP_TYPES = BROTLI_TYPES  # same mapping for gzip


class UnityWebGLHandler(http.server.SimpleHTTPRequestHandler):

    def end_headers(self):
        path = self.path.split("?")[0]  # strip query string

        if path.endswith(".br"):
            base = path[:-3]  # strip .br
            # pick content type by the real extension
            for ext, mime in BROTLI_TYPES.items():
                if base.endswith(ext):
                    self.send_header("Content-Type", mime)
                    break
            else:
                self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Encoding", "br")

        elif path.endswith(".gz"):
            base = path[:-3]
            for ext, mime in GZIP_TYPES.items():
                if base.endswith(ext):
                    self.send_header("Content-Type", mime)
                    break
            else:
                self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Encoding", "gzip")

        # Shared response headers
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Suppress noisy 304s; keep errors visible
        if args and str(args[1]) not in ("200", "206", "304"):
            super().log_message(fmt, *args)


os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), UnityWebGLHandler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving Unity WebGL build at  http://localhost:{PORT}")
    print("Press Ctrl+C to stop.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
