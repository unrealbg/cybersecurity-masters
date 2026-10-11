# Week 1 — Verification

Status: **NOT YET VERIFIED**

## Networking evidence

### Ubuntu

```text
Interfaces:
ens33  192.168.153.129/24   (NAT-facing)
ens37  192.168.56.10/24     (CyberLab)

Routes:
default via 192.168.153.2 dev ens33
192.168.56.0/24 dev ens37
192.168.153.0/24 dev ens33

Observed listening sockets:
TCP: 0.0.0.0:22, [::]:22
UDP: 127.0.0.53:53, 127.0.0.54:53, 192.168.153.129%ens33:68, 127.0.0.1:323, [::1]:323
TCP DNS stub listeners: 127.0.0.53:53, 127.0.0.54:53

Process ownership from `sudo ss -tulpn`:
- systemd-resolved -> DNS stub listeners on 127.0.0.53:53 / 127.0.0.54:53
- systemd-networkd -> DHCP client UDP socket on 192.168.153.129%ens33:68
- chronyd -> NTP-related local sockets on 127.0.0.1:323 / [::1]:323
- systemd (PID 1) -> TCP listeners on 0.0.0.0:22 / [::]:22, consistent with socket-activated SSH

Link-layer observations:
ens33 MAC 00:0c:29:b5:7d:50
ens37 MAC 00:0c:29:b5:7d:5a
```

### Kali

```text
Interfaces:
eth0  192.168.153.130/24   (NAT-facing)
eth1  192.168.56.20/24     (CyberLab)

Routes:
default via 192.168.153.2 dev eth0
192.168.56.0/24 dev eth1
192.168.153.0/24 dev eth0

Link-layer observations:
eth0 MAC 00:0c:29:07:6b:e5
eth1 MAC 00:0c:29:07:6b:ef

Listening sockets from `sudo ss -tulpn`: none observed at capture time.
```

### Windows

```text
Interfaces:
NAT       192.168.153.132/24   (DHCP, ifIndex 12)
CyberLab  192.168.56.30/24     (static, ifIndex 10)

Default route:
0.0.0.0/0 -> 192.168.153.2 via NAT (ifIndex 12)

Directly connected routes:
192.168.153.0/24 via NAT
192.168.56.0/24 via CyberLab

Selected TCP listeners:
135/tcp on 0.0.0.0 and :: -> PID 500 svchost
139/tcp on 192.168.153.132 and 192.168.56.30 -> PID 4 System
445/tcp on :: -> PID 4 System
5040/tcp on 0.0.0.0 -> PID 4904 svchost
7680/tcp on :: -> PID 5720 svchost
42050/tcp on ::1 -> PID 6976 OneDrive.Sync.Service
49664/tcp on 0.0.0.0 and :: -> PID 832 lsass
49665/tcp on 0.0.0.0 and :: -> PID 676 wininit
49666/tcp on 0.0.0.0 and :: -> PID 1440 svchost
49667/tcp on 0.0.0.0 and :: -> PID 1828 svchost
49668/tcp on 0.0.0.0 and :: -> PID 2832 spoolsv
49669/tcp on 0.0.0.0 and :: -> PID 812 services

Selected UDP endpoints:
137/udp and 138/udp on both IPv4 interfaces
1900/udp on both IPv4 interfaces plus loopback/link-local
5353/udp on 0.0.0.0 and ::
5355/udp on 0.0.0.0 and ::
```

### ARP observation

Ubuntu CyberLab interface: `ens37` (`192.168.56.10/24`)  
Kali CyberLab address: `192.168.56.20/24`

Observed after starting with no Kali neighbor entry and sending one ICMP echo:

```text
ARP Request: who-has 192.168.56.20 tell 192.168.56.10
ARP Reply:   192.168.56.20 is-at 00:0c:29:07:6b:ef
```

Neighbor cache after the exchange:

```text
192.168.56.20 dev ens37 lladdr 00:0c:29:07:6b:ef REACHABLE
```

A later reverse ARP exchange was also captured:

```text
ARP Request: who-has 192.168.56.10 tell 192.168.56.20
ARP Reply:   192.168.56.10 is-at 00:0c:29:b5:7d:5a
```

This demonstrates direct on-link IPv4 delivery: route selection chooses `ens37`, ARP resolves the peer IPv4 address to a Layer-2 MAC address, and no gateway is involved.


### Traceroute observation

A standard UDP traceroute from Ubuntu to `8.8.8.8` reached the VMware NAT gateway as hop 1 and then timed out:

```text
1  _gateway (192.168.153.2)
2-30  * * *
```

ICMP traceroute reached the destination despite missing replies from intermediate hops:

```text
1  _gateway (192.168.153.2)
2-8  * * *
9  dns.google (8.8.8.8)
```

TCP traceroute to port 443 reached the destination immediately after the VMware NAT gateway:

```text
1  _gateway (192.168.153.2)
2  dns.google (8.8.8.8)
```

A direct ping also succeeded with 4/4 replies and 0% packet loss.

These observations show that traceroute visibility depends on probe type and on how NAT/firewalls/intermediate network devices handle TTL-expired and probe traffic. A `* * *` hop indicates that no expected response was received within the timeout; it does not by itself prove that routing stops at that hop.


### Route lookup and next-hop neighbor

A live route lookup for `8.8.8.8` returned:

```text
8.8.8.8 via 192.168.153.2 dev ens33 src 192.168.153.128 uid 1000
```

The corresponding next-hop neighbor entry was:

```text
192.168.153.2 dev ens33 lladdr 00:50:56:f3:c7:3c REACHABLE
```

This demonstrates that the remote IP destination remains `8.8.8.8`, while the first Ethernet frame is addressed to the MAC of the next-hop gateway `192.168.153.2`.

Follow-up confirmation with `ip -br addr show ens33` showed `ens33 192.168.153.128/24`. The earlier `192.168.153.129` entry is therefore preserved as a point-in-time DHCP lease; the current observed NAT-interface address is `192.168.153.128/24`.

## Route prediction

- [ ] Predictions were written before checking the routing tables.
- [ ] Directly connected CyberLab destinations were correctly identified.
- [ ] Internet destinations were correctly identified as using the NAT/default route.

## Python refresher

- [ ] `system_info.py` was extended by the student.
- [ ] Two new fields were added without hard-coded values.
- [ ] Output remains valid JSON.
- [ ] Invalid user input was handled in the mini exercise.
- [ ] Port range `1..65535` was validated.

## Self-check

Mark only after explaining each answer in your own words.

- [ ] IP address vs MAC address
- [ ] port and process/application relationship
- [ ] TCP vs UDP
- [ ] frame vs packet
- [ ] directly connected route vs default route
- [ ] why CyberLab has no default gateway
- [ ] why structured JSON is useful

## Result

- [ ] PASS — Week 1 complete.
- [ ] NEEDS WORK

### Notes

```text
Ubuntu Week 1 networking evidence captured from the live CyberLab.
ARP resolution between Ubuntu and Kali was observed live on the isolated CyberLab segment.
```
