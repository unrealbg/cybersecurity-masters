# Week 0 — VMware Workstation Setup

This guide implements the Week 0 CyberLab topology with VMware Workstation.

## Target design

Each VM has two adapters:

1. **NAT** — VMware's NAT network (normally VMnet8)
2. **Host-only** — isolated CyberLab network

```text
                         Internet
                            |
                          VMnet8
                            |
                     VMware NAT
                     /      |       \
                 Ubuntu    Kali    Windows
                   |        |        |
                   +--------+--------+
                            |
                 CyberLab Host-only
                    192.168.56.0/24
```

## 1. Create the CyberLab host-only network

Open:

`Edit -> Virtual Network Editor`

Choose an unused VMnet for the lab instead of changing the default NAT network.

Recommended:

```text
VMnet2
Type: Host-only
Subnet IP: 192.168.56.0
Subnet mask: 255.255.255.0
DHCP: disabled
```

If VMnet2 already exists for another purpose, use another unused custom VMnet and document it.

### Settings

- Host-only: enabled
- Subnet: `192.168.56.0`
- Mask: `255.255.255.0`
- VMware DHCP: disabled for this lab
- NAT: disabled on the lab VMnet

Whether the VMware host virtual adapter is connected to VMnet2 is optional for the course. Keeping it enabled makes host-to-VM troubleshooting easier, but it also means the host participates in the lab subnet.

## 2. Ubuntu VM adapters

Power off the VM before changing its virtual hardware.

Open:

`VM -> Settings`

### Network Adapter 1

```text
Network connection: NAT
Connect at power on: yes
```

### Network Adapter 2

Add:

`Add -> Network Adapter -> Custom: Specific virtual network -> VMnet2`

```text
Connect at power on: yes
```

Inside Ubuntu configure the VMnet2-facing interface as:

```text
192.168.56.10/24
gateway: none
DNS: none
```

The NAT-facing interface should remain DHCP.

## 3. Kali VM adapters

Use the same VMware adapter arrangement.

Lab interface:

```text
192.168.56.20/24
gateway: none
DNS: none
```

## 4. Windows VM adapters

Use the same VMware adapter arrangement.

Lab interface:

```text
IP: 192.168.56.30
Mask: 255.255.255.0
Default gateway: blank
DNS: blank
```

## 5. Verification

### Ubuntu / Kali

```bash
ip -br addr
ip route
```

Expected shape:

```text
<nat-interface>   <VMware DHCP address>
<lab-interface>   192.168.56.x/24

default via <VMware NAT gateway> dev <nat-interface>
192.168.56.0/24 dev <lab-interface>
```

Peer tests:

```bash
ping -c 3 192.168.56.10
ping -c 3 192.168.56.20
ping -c 3 192.168.56.30
```

Skip the machine's own address.

### Windows

```powershell
Get-NetIPAddress -AddressFamily IPv4
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
Test-Connection 192.168.56.10 -Count 3
Test-Connection 192.168.56.20 -Count 3
```

Windows Firewall may block ICMP. Treat that separately from basic interface/routing verification.

## 6. Snapshot baseline

After installing updates and verifying networking, create a snapshot for each VM:

```text
week-00-clean-baseline
```

Do this before adding intentionally vulnerable services or changing defensive controls.

## Expected final inventory

| VM | NAT | CyberLab VMnet2 |
|---|---|---|
| Ubuntu | DHCP | 192.168.56.10/24 |
| Kali | DHCP | 192.168.56.20/24 |
| Windows | DHCP | 192.168.56.30/24 |

Record actual evidence in `05-security-labs/week-00-verification.md`.
