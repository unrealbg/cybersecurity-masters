# Logging and Detection Lab

## Goal

Learn how normal and abnormal authentication events appear in operating-system logs.

## Tasks

1. Generate several successful and failed logins in the isolated lab.
2. Locate the relevant Linux or Windows logs.
3. Record timestamp, account, source address (if present) and result.
4. Write a parser that counts failed attempts by source/account.
5. Export a small JSON summary.

## Defensive questions

- What constitutes a useful threshold?
- What legitimate behavior may cause false positives?
- What additional context would improve confidence?
