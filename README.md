# Cybersecurity Master's Labs

Practical study repository accompanying my master's program in **Cybersecurity: Technologies in the Financial Sector**.

The goal of this repository is to turn university theory into reproducible labs, small tools, technical notes, and portfolio-ready exercises.

## Semester 1 focus

- Programming for cybersecurity (Python)
- Databases and data security
- Computer networks and communications
- Computer infrastructure (Linux / Windows)
- Introductory security labs

## Repository structure

```text
01-programming/       Python exercises and small security-oriented tools
02-databases/         Database security notes and local labs
03-networking/        TCP/IP, DNS, routing, Wireshark and packet analysis
04-infrastructure/    Linux/Windows administration and hardening notes
05-security-labs/     Cross-topic practical labs
notes/                Short study notes and revision material
docs/                 Study plans and roadmaps
templates/             Reusable lab-report template
.github/workflows/    Lightweight validation for Python files
```

## Lab environment

Each VM uses a NAT adapter for updates plus a separate isolated lab adapter:

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

Week 0 setup guide: [`docs/week-00-cyberlab-setup.md`](docs/week-00-cyberlab-setup.md)

Verification worksheet: [`05-security-labs/week-00-verification.md`](05-security-labs/week-00-verification.md)

Use intentionally vulnerable services **only inside an isolated lab you control**.

## Semester 1 roadmap

- [ ] Week 0 — Lab environment and repository setup
- [ ] Week 1 — TCP/IP basics + Python refresher
- [ ] Week 2 — IPv4, subnetting, ARP and ICMP
- [ ] Week 3 — DNS, DHCP and Python sockets
- [ ] Week 4 — HTTP, HTTPS and TLS
- [ ] Week 5 — Linux infrastructure
- [ ] Week 6 — Windows infrastructure
- [ ] Week 7 — Database security and SQL injection concepts
- [ ] Week 8 — Wireshark packet analysis
- [ ] Week 9 — Routing, NAT and firewalling
- [ ] Week 10 — Logging and detection
- [ ] Week 11 — Cryptography fundamentals
- [ ] Week 12 — Consolidation
- [ ] Week 13 — Mini project: HostInspector
- [ ] Week 14 — Exam revision

## Conventions

Each lab should contain:

1. Goal
2. Environment
3. Commands / code used
4. Evidence or output
5. Explanation of what happened
6. Security relevance
7. What I learned

A reusable template is available in [`templates/lab-report-template.md`](templates/lab-report-template.md).
