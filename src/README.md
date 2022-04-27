# Package Management System

## How to use

Add desired packages into `packages.yml` with this format:

```yml
packages:
  - name: <required>
    packageName: <required>
    packageManager: <optional>
    test:
      command: <required>
      expected_status: <optional>
```
