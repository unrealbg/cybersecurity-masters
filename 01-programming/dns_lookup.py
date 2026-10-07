#!/usr/bin/env python3
"""Resolve a hostname and print unique IPv4/IPv6 addresses."""

from __future__ import annotations

import argparse
import socket
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve a hostname using the system resolver.")
    parser.add_argument("hostname", help="Hostname to resolve, e.g. example.com")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        records = socket.getaddrinfo(args.hostname, None, proto=socket.IPPROTO_TCP)
    except socket.gaierror as exc:
        print(f"DNS lookup failed: {exc}", file=sys.stderr)
        return 1

    addresses = sorted({record[4][0] for record in records})
    print(f"Hostname: {args.hostname}")
    for address in addresses:
        print(address)

    return 0


if __name__ == "__main__":
    sys.exit(main())
