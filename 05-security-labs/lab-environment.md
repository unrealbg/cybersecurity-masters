# Cyber Lab Environment

## Suggested topology

Each VM uses two adapters:

- **NAT NIC** — outbound Internet access for updates.
- **Isolated lab NIC** — VM-to-VM training traffic only.

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

The isolated NIC must not be bridged to the physical LAN.

## Address plan

| VM | Isolated lab address |
|---|---|
| Ubuntu | `192.168.56.10/24` |
| Kali | `192.168.56.20/24` |
| Windows | `192.168.56.30/24` |

Do **not** configure a default gateway on the isolated NIC. The default route should remain on the NAT-facing interface.

## Suggested roles

- **Ubuntu** — Linux server, SSH, logs, database or local test application
- **Windows** — workstation / Windows administration labs
- **Kali** — security tooling inside the isolated lab only

## Baseline checklist

- [ ] Hypervisor selected
- [ ] NAT enabled where needed
- [ ] Isolated host-only/internal/private network created
- [ ] Lab NIC is not bridged to the physical LAN
- [ ] Lab IP addresses documented
- [ ] Default route uses the NAT interface
- [ ] VM snapshots created before risky exercises
- [ ] No sensitive host folders shared into intentionally vulnerable VMs

## Week 0

Follow the complete setup procedure in [`docs/week-00-cyberlab-setup.md`](../docs/week-00-cyberlab-setup.md).

Record real verification evidence in [`week-00-verification.md`](week-00-verification.md).
