# Week 0 — CyberLab Setup

## Goal

Build a small, repeatable lab for the first semester with three virtual machines:

- Ubuntu — server and defensive Linux work
- Kali Linux — security tooling inside the isolated lab
- Windows — workstation and Windows administration/security work

The lab must separate experimental traffic from the normal home/office network.

## Recommended topology

Each VM gets **two virtual NICs**:

1. **NIC 1 — NAT**  
   Used for OS/package updates and ordinary outbound Internet access.

2. **NIC 2 — isolated lab network**  
   Used only for VM-to-VM exercises.

```text
                         Internet
                            |
                      Hypervisor NAT
                     /      |       \
                 Ubuntu    Kali    Windows
                   |        |        |
                   +--------+--------+
                            |
                 CYBERLAB 192.168.56.0/24
```

Do not bridge the isolated lab interface to the physical LAN.

VMware Workstation users: follow the dedicated guide in [`week-00-vmware-workstation.md`](week-00-vmware-workstation.md).

## Hypervisor terminology

Use the equivalent isolated-network mode for your hypervisor:

| Hypervisor | Suitable lab-network type |
|---|---|
| VirtualBox | Internal Network or Host-only |
| VMware Workstation | Host-only |
| Hyper-V | Private vSwitch; Internal vSwitch if host access is deliberately required |

For the first labs, prefer a network that **does not expose the VMs directly to the physical LAN**.

## Address plan

Use these addresses on the isolated lab interface:

| VM | Lab IPv4 | Prefix | Default gateway on lab NIC |
|---|---:|---:|---|
| Ubuntu | 192.168.56.10 | /24 | none |
| Kali | 192.168.56.20 | /24 | none |
| Windows | 192.168.56.30 | /24 | none |

The NAT adapter may receive its address automatically from the hypervisor.

Do not configure a DNS server on the isolated interface unless a later lab explicitly requires one.

## Suggested VM resources

These are practical starting points, not hard requirements:

| VM | vCPU | RAM | Disk |
|---|---:|---:|---:|
| Ubuntu | 2 | 4 GB | 30 GB |
| Kali | 2 | 4 GB | 40 GB |
| Windows | 2–4 | 6–8 GB | 64 GB |

Reduce these values if the host cannot comfortably run all three VMs simultaneously.

## Setup order

### 1. Prepare the hypervisor

- [ ] Confirm hardware virtualization is enabled.
- [ ] Create the isolated network.
- [ ] Confirm it is **not bridged** to the physical adapter.
- [ ] Keep NAT available separately for Internet access.

### 2. Create Ubuntu VM

- [ ] Install Ubuntu.
- [ ] Attach NAT + isolated NIC.
- [ ] Configure lab address: `192.168.56.10/24`.
- [ ] Do not add a default gateway to the lab NIC.
- [ ] Install pending updates.
- [ ] Create a clean baseline snapshot.

Record:

```text
Hostname:
OS/version:
NAT address:
Lab address: 192.168.56.10/24
Snapshot:
```

### 3. Create Kali VM

- [ ] Install/import Kali.
- [ ] Attach NAT + isolated NIC.
- [ ] Configure lab address: `192.168.56.20/24`.
- [ ] Do not add a default gateway to the lab NIC.
- [ ] Install pending updates.
- [ ] Create a clean baseline snapshot.

Record:

```text
Hostname:
OS/version:
NAT address:
Lab address: 192.168.56.20/24
Snapshot:
```

### 4. Create Windows VM

- [ ] Install Windows.
- [ ] Attach NAT + isolated NIC.
- [ ] Configure lab address: `192.168.56.30/24`.
- [ ] Do not add a default gateway to the lab NIC.
- [ ] Install pending updates.
- [ ] Create a clean baseline snapshot.

Record:

```text
Hostname:
OS/version:
NAT address:
Lab address: 192.168.56.30/24
Snapshot:
```

## Verification

### Linux

Run on Ubuntu and Kali:

```bash
ip addr
ip route
ping -c 3 192.168.56.10
ping -c 3 192.168.56.20
ping -c 3 192.168.56.30
```

A VM should not ping itself as a substitute for peer verification; test only the two other peers as appropriate.

Check that the default route belongs to the NAT-facing interface:

```bash
ip route | grep default
```

### Windows

Run in PowerShell:

```powershell
Get-NetIPAddress -AddressFamily IPv4
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
Test-Connection 192.168.56.10 -Count 3
Test-Connection 192.168.56.20 -Count 3
```

The default route should use the NAT-facing adapter, not the lab adapter.

## Important Windows note

Windows Firewall may block ICMP echo by default. A failed ping does **not** automatically mean the virtual network is broken.

If Ubuntu/Kali can communicate and Windows has the expected `192.168.56.30/24` address, inspect the Windows firewall profile/rules before changing the topology.

## Isolation checks

Before using intentionally vulnerable software later in the course:

- [ ] No VM lab NIC is bridged to the physical LAN.
- [ ] No default gateway exists on the isolated NIC.
- [ ] Shared folders do not expose sensitive host directories.
- [ ] Clipboard/drag-and-drop sharing is disabled when a risky lab does not need it.
- [ ] Baseline snapshots exist.
- [ ] Real credentials, SSH keys, tokens and private files are not copied into lab VMs.

## Week 0 completion criteria

Week 0 is complete only when:

- [ ] all three VMs exist;
- [ ] NAT Internet access works where needed;
- [ ] all three isolated addresses are configured;
- [ ] peer connectivity is verified or any deliberate firewall exception is documented;
- [ ] routing tables show NAT as the Internet path;
- [ ] baseline snapshots exist;
- [ ] the results are recorded in the Week 0 verification report.

Use [`templates/lab-report-template.md`](../templates/lab-report-template.md) for additional notes.
