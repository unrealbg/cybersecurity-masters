# Wireshark Lab

## Goal

Observe a normal client connection from name resolution to encrypted application traffic.

## Capture checklist

- [ ] ARP (when applicable)
- [ ] DNS query and response
- [ ] TCP SYN
- [ ] TCP SYN/ACK
- [ ] TCP ACK
- [ ] TLS traffic

## Useful display filters

```text
arp
icmp
dns
tcp
tcp.port == 443
ip.addr == 192.168.56.10
```

## Questions

1. Which host initiated the TCP connection?
2. Which destination port was used?
3. Which packets form the TCP three-way handshake?
4. Can the HTTP application data be read when TLS is used?
5. Which metadata remains visible even when payloads are encrypted?

## Evidence

Add screenshots or packet numbers here. Do not commit captures containing private credentials or unrelated personal traffic.
