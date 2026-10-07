# TCP/IP Quick Reference

| Layer | Typical examples | Questions to ask |
|---|---|---|
| Application | DNS, HTTP, SSH | What protocol and application semantics are used? |
| Transport | TCP, UDP | Which ports? Is delivery connection-oriented? |
| Internet | IPv4, IPv6, ICMP | Which hosts/networks are communicating? |
| Link | Ethernet, ARP | How is the next local hop reached? |

## Core terms

- **MAC address** — link-layer identifier used on the local network.
- **IP address** — logical network-layer address.
- **Port** — transport-layer endpoint identifier.
- **Default gateway** — next-hop router used when the destination is outside the local route.
- **DNS** — maps names to records such as A/AAAA/MX/TXT.
- **ARP** — resolves an IPv4 address to a local link-layer address.
