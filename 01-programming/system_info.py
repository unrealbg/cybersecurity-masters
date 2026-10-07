#!/usr/bin/env python3
"""Display basic local host information using only the standard library."""

from __future__ import annotations

import json
import platform
import socket
import sys


def get_local_ip() -> str:
    """Best-effort discovery of the preferred local IPv4 address."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No packet needs to be sent for connect() on a UDP socket.
        sock.connect(("192.0.2.1", 80))
        return str(sock.getsockname()[0])
    except OSError:
        try:
            return socket.gethostbyname(socket.gethostname())
        except OSError:
            return "unknown"
    finally:
        sock.close()


def collect_system_info() -> dict[str, str]:
    return {
        "hostname": socket.gethostname(),
        "os": platform.platform(),
        "python": platform.python_version(),
        "local_ip": get_local_ip(),
    }


def main() -> int:
    print(json.dumps(collect_system_info(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
