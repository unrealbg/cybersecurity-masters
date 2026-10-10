# Week 0 — CyberLab Verification

Status: **NOT YET VERIFIED**

> Complete this file after the three VMs have actually been created. Do not mark items complete from the design alone.

## Environment

Hypervisor: VMware Workstation

Host OS: Windows

Date verified: 2026-10-10

## Address inventory

| System | Hostname | NAT IPv4 | Lab IPv4 | Baseline snapshot |
|---|---|---|---|---|
| Ubuntu | cyber-ubuntu | 192.168.153.129/24 | 192.168.56.10/24 | pending |
| Kali | cyber-kali | 192.168.153.130/24 | 192.168.56.20/24 | pending |
| Windows | CYBER-WIN10 | 192.168.153.132/24 | 192.168.56.30/24 | pending |

## Connectivity matrix

Record PASS / BLOCKED-BY-FIREWALL / FAIL.

| Source → Destination | Ubuntu | Kali | Windows |
|---|---|---|---|
| Ubuntu | N/A | PASS | BLOCKED-BY-FIREWALL |
| Kali | PASS | N/A | BLOCKED-BY-FIREWALL |
| Windows | PASS | PASS | N/A |

## Routing evidence

### Ubuntu

```text
default via 192.168.153.2 dev ens33 proto dhcp src 192.168.153.129 metric 100
192.168.56.0/24 dev ens37 proto kernel scope link src 192.168.56.10
192.168.153.0/24 dev ens33 proto kernel scope link src 192.168.153.129 metric 100
192.168.153.2 dev ens33 proto dhcp scope link src 192.168.153.129 metric 100
```

Observed interfaces:

```text
ens33  192.168.153.129/24
ens37  192.168.56.10/24
```

### Kali

```text
default via 192.168.153.2 dev eth0 proto dhcp src 192.168.153.130 metric 101
192.168.56.0/24 dev eth1 proto kernel scope link src 192.168.56.20 metric 102
192.168.153.0/24 dev eth0 proto kernel scope link src 192.168.153.130 metric 101
```

Observed interfaces:

```text
eth0  192.168.153.130/24
eth1  192.168.56.20/24
```

### Windows

```text
Default route:
0.0.0.0/0 -> 192.168.153.2 via NAT (ifIndex 11)

Observed interfaces:
NAT       192.168.153.132/24
CyberLab  192.168.56.30/24
```

## Isolation checklist

- [x] Isolated lab NICs are not bridged to the physical LAN.
- [x] Lab NICs have no default gateway.
- [x] NAT is the Internet-facing path.
- [ ] Baseline snapshots exist.
- [ ] Sensitive host folders are not shared into risky lab VMs.
- [ ] No real secrets/credentials have been copied into the lab.

## Result

- [ ] PASS — Week 0 CyberLab baseline is ready.
- [x] NEEDS WORK — document the problem below.

### Notes / problems

```text
Windows can reach Ubuntu and Kali over VMnet2.
Ubuntu and Kali can reach each other.
Inbound ICMP echo to Windows is currently blocked by Windows Firewall.
Allow ICMPv4 echo only on the CyberLab interface/subnet, then retest.
```
