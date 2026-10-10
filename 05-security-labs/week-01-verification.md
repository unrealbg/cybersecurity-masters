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
paste concise output / observations here
```

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
```
