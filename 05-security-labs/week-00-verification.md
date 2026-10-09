# Week 0 — CyberLab Verification

Status: **NOT YET VERIFIED**

> Complete this file after the three VMs have actually been created. Do not mark items complete from the design alone.

## Environment

Hypervisor:

Host OS:

Date verified:

## Address inventory

| System | Hostname | NAT IPv4 | Lab IPv4 | Baseline snapshot |
|---|---|---|---|---|
| Ubuntu | cyber-ubuntu | 192.168.153.129/24 | 192.168.56.10/24 | pending |
| Kali |  |  | 192.168.56.20/24 |  |
| Windows |  |  | 192.168.56.30/24 |  |

## Connectivity matrix

Record PASS / BLOCKED-BY-FIREWALL / FAIL.

| Source → Destination | Ubuntu | Kali | Windows |
|---|---|---|---|
| Ubuntu | N/A |  |  |
| Kali |  | N/A |  |
| Windows |  |  | N/A |

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
paste: ip route
```

### Windows

```text
paste: Get-NetRoute -DestinationPrefix "0.0.0.0/0"
```

## Isolation checklist

- [ ] Isolated lab NICs are not bridged to the physical LAN.
- [ ] Lab NICs have no default gateway.
- [ ] NAT is the Internet-facing path.
- [ ] Baseline snapshots exist.
- [ ] Sensitive host folders are not shared into risky lab VMs.
- [ ] No real secrets/credentials have been copied into the lab.

## Result

- [ ] PASS — Week 0 CyberLab baseline is ready.
- [ ] NEEDS WORK — document the problem below.

### Notes / problems

```text

```
