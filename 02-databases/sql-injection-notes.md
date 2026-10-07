# SQL Injection — Study Notes

## Root cause

SQL injection occurs when untrusted input is treated as SQL syntax instead of data.

Unsafe pattern (conceptual):

```text
query = "SELECT ... WHERE username = '" + input + "'"
```

Preferred pattern:

- parameterized queries / prepared statements
- strict authorization checks
- least-privilege database accounts
- safe secret storage
- useful server-side logging

## Lab objective

Build a tiny local application twice:

1. an intentionally unsafe version for observation inside the isolated lab;
2. a corrected version using parameterization.

Document the difference rather than publishing reusable attack payloads.
