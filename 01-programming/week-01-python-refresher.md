# Week 1 — Python Refresher

## Primary task

Read `system_info.py` and make two small extensions yourself.

Required:

- add two useful system-information fields;
- keep the return value of `collect_system_info()` as a dictionary;
- keep the output valid JSON;
- use only the Python standard library.

Run:

```bash
python 01-programming/system_info.py
```

The output should still be parseable JSON.

## Mini exercises

Do these in a scratch file or Python REPL.

### 1. List + loop

Given:

```python
hosts = ["ubuntu", "kali", "windows"]
```

Print one host per line with its position.

### 2. Dictionary

Represent the CyberLab static addresses as a dictionary:

```text
ubuntu  -> 192.168.56.10
kali    -> 192.168.56.20
windows -> 192.168.56.30
```

Then look up Kali's address by key.

### 3. Function

Write:

```python
def endpoint(ip: str, port: int) -> str:
    ...
```

Expected example:

```text
endpoint("192.168.56.10", 22)
-> 192.168.56.10:22
```

### 4. Validation + exception

Ask the user for a port and convert it to an integer.

Handle invalid input instead of crashing.

Then reject values outside:

```text
1..65535
```

### 5. JSON

Serialize the CyberLab host dictionary with `json.dumps(..., indent=2)`.

Then explain why structured JSON is more useful for automation than human-only formatted output.

## Reflection

Answer briefly:

- When would you choose a list instead of a dictionary?
- What does a function buy us over repeated inline code?
- Why should security tooling handle malformed input explicitly?
- Why is machine-readable output useful for logs, APIs and automation?
