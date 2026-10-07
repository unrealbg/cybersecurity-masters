#!/usr/bin/env python3
"""Show useful information about an IPv4 or IPv6 network."""

from __future__ import annotations

import argparse
import ipaddress
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Display network information for an address in CIDR notation."
    )
    parser.add_argument("network", help="Example: 192.168.10.20/27")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        interface = ipaddress.ip_interface(args.network)
    except ValueError as exc:
        print(f"Invalid network: {exc}", file=sys.stderr)
        return 2

    network = interface.network
    print(f"Address:    {interface.ip}")
    print(f"Network:    {network.network_address}/{network.prefixlen}")
    print(f"Netmask:    {network.netmask}")
    print(f"Addresses:  {network.num_addresses}")

    if isinstance(network, ipaddress.IPv4Network):
        print(f"Broadcast:  {network.broadcast_address}")
        usable = max(network.num_addresses - 2, 0) if network.prefixlen <= 30 else network.num_addresses
        print(f"Usable*:    {usable}")
        print("*Conventional IPv4 host count; /31 and /32 have special semantics.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
