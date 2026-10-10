# Week 1 Lab — TCP/IP Observation

## Goal

Observe how each CyberLab machine is addressed and how the operating system chooses between the NAT and isolated CyberLab networks.

## Known topology

```text
Ubuntu
  NAT       192.168.153.129/24
  CyberLab  192.168.56.10/24

Kali
  NAT       192.168.153.130/24
  CyberLab  192.168.56.20/24

Windows
  NAT       192.168.153.132/24
  CyberLab  192.168.56.30/24
```

The NAT addresses may change after DHCP renewal. The CyberLab addresses are static.

## Part 1 — Ubuntu

Run:

```bash
ip -br addr
ip route
ip link
ss -tuln
```

Record:

- NAT interface:
- CyberLab interface:
- default gateway:
- directly connected networks:
- listening TCP ports:
- listening UDP ports:

### Questions

1. Why does `192.168.56.0/24` not need a gateway?
2. Which route is used for `192.168.56.20`?
3. Which route is used for `1.1.1.1`?
4. Does a listening port automatically mean the service is reachable from every interface?

## Part 2 — Kali

Run:

```bash
ip -br addr
ip route
ip link
ss -tuln
```

Record:

- NAT interface:
- CyberLab interface:
- default gateway:
- directly connected networks:

Then test:

```bash
ping -c 3 192.168.56.10
ping -c 3 192.168.56.30
```

Explain why this traffic should stay on VMnet2 instead of using the NAT gateway.

## Part 3 — Windows

Run in PowerShell:

```powershell
Get-NetAdapter
Get-NetIPAddress -AddressFamily IPv4
Get-NetRoute -AddressFamily IPv4
Get-NetTCPConnection -State Listen
```

Record:

- NAT adapter:
- CyberLab adapter:
- default gateway:
- CyberLab route:

Then:

```powershell
Test-Connection 192.168.56.10 -Count 3
Test-Connection 192.168.56.20 -Count 3
```

## Part 4 — route prediction

Before running any additional command, predict the interface for each destination.

| Source | Destination | Your predicted interface | Why? |
|---|---|---|---|
| Ubuntu | 192.168.56.20 |  |  |
| Ubuntu | 192.168.153.2 |  |  |
| Ubuntu | 1.1.1.1 |  |  |
| Kali | 192.168.56.30 |  |  |
| Kali | 8.8.8.8 |  |  |
| Windows | 192.168.56.10 |  |  |
| Windows | 1.1.1.1 |  |  |

After predicting, compare your answers against the routing tables.

## Part 5 — vocabulary from evidence

For one successful Kali → Ubuntu ping, identify:

- source IP:
- destination IP:
- protocol:
- source MAC:
- destination MAC:
- whether a TCP/UDP port exists for this traffic:
- which TCP/IP layer ICMP belongs to:

You may use `ip neigh` / ARP information if needed. Packet capture is reserved for a later Wireshark-focused week.

## Result

- [ ] PASS
- [ ] NEEDS WORK

### What I learned

Write 5–10 sentences in your own words.
