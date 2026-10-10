# Week 1 — TCP/IP Basics + Python Refresher

## Goal

Build a working mental model of how application traffic moves through the TCP/IP stack and refresh the Python fundamentals needed for later cybersecurity exercises.

## Learning outcomes

By the end of Week 1 you should be able to:

- explain the TCP/IP layers in your own words;
- distinguish frame, packet, segment/datagram and application data;
- explain the roles of MAC address, IP address and port;
- distinguish TCP from UDP at a high level;
- identify the local interface, route and default gateway used for a destination;
- read simple output from `ip`, `ss`, `ping` and Windows networking commands;
- use Python variables, lists, dictionaries, functions, exceptions, modules and JSON;
- explain what `system_info.py` does and extend it without copying a solution.

## Time budget

Target: about 6–7 hours total.

| Block | Time | Focus |
|---|---:|---|
| A | 90 min | TCP/IP theory |
| B | 90 min | Python refresher |
| C | 2–3 h | CyberLab networking exercise |
| D | 60 min | Notes, self-check and Git commit |

## Block A — TCP/IP mental model

Use this four-layer model:

```text
Application   DNS / HTTP / SSH
Transport     TCP / UDP
Internet      IPv4 / IPv6 / ICMP
Link          Ethernet / ARP
```

For a browser connecting to an HTTPS server, reason about:

```text
Application data
      ↓
TCP segment
      ↓
IP packet
      ↓
Ethernet frame
      ↓
physical / virtual link
```

### Terms you must be able to explain

- hostname
- IP address
- subnet/prefix
- MAC address
- port
- protocol
- route
- default gateway
- frame
- packet
- TCP segment
- UDP datagram

Do not memorize definitions mechanically. For each term, answer: **what problem does it solve?**

## Block B — Python refresher

Review:

- strings, integers and booleans;
- lists, tuples, sets and dictionaries;
- `if`, `for` and `while`;
- functions and return values;
- exceptions;
- imports/modules;
- file I/O;
- JSON.

Read `01-programming/system_info.py` line by line.

Then extend it yourself with **two** additional fields of your choice, for example:

- current username;
- machine architecture;
- fully qualified hostname;
- processor description.

Constraints:

- use only the standard library;
- do not hard-code the values;
- keep `collect_system_info()` returning structured data;
- keep JSON output valid.

## Block C — CyberLab

Use Ubuntu, Kali and Windows from Week 0.

Follow:

[`03-networking/week-01-tcpip-lab.md`](../03-networking/week-01-tcpip-lab.md)

The important part is not producing screenshots. It is explaining what each command proves.

## Block D — self-check

Without looking at notes, answer:

1. Why can two applications on one IP address communicate independently?
2. What is the practical difference between an IP address and a MAC address?
3. When does a host use its default gateway?
4. Why does the CyberLab NIC have no default gateway?
5. What is the difference between TCP and UDP?
6. What is the difference between a packet and a frame?
7. Which interface does Ubuntu use for Internet access?
8. Which interface does Kali use for CyberLab traffic?
9. Why is JSON useful for security automation?
10. What does an exception prevent when handled correctly in Python?

If you cannot explain an answer in 2–4 sentences, revisit that topic.

## Week 1 completion criteria

- [ ] TCP/IP terms explained in your own notes.
- [ ] Ubuntu network observations recorded.
- [ ] Kali network observations recorded.
- [ ] Windows network observations recorded.
- [ ] Route-selection exercise completed.
- [ ] `system_info.py` extended with two fields.
- [ ] Python script still runs and emits valid JSON.
- [ ] Self-check completed without relying heavily on notes.
- [ ] Week 1 lab report committed to Git.

Do not mark Week 1 complete merely because the commands were executed. The acceptance criterion is understanding what the outputs mean.
