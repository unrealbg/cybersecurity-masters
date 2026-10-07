# Cyber Lab Environment

## Suggested topology

```text
                  Internet
                     |
                   NAT
                     |
             Virtual Lab Network
              192.168.56.0/24
             /        |        \
        Ubuntu       Kali     Windows
```

## Suggested roles

- **Ubuntu** — Linux server, SSH, logs, database or local test application
- **Windows** — workstation / Windows administration labs
- **Kali** — security tooling inside the isolated lab only

## Baseline checklist

- [ ] Hypervisor selected
- [ ] NAT enabled where needed
- [ ] Isolated host-only/internal network created
- [ ] VM snapshots created before risky exercises
- [ ] IP addresses documented
- [ ] No sensitive host folders shared into intentionally vulnerable VMs
