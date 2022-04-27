# Package Management System

## How to use

Add desired packages into `packages.yml` with this format:

```yml
packages:
  - name: <required>
    manager:
      name: <required>
      options: <optional>
    installatonTest:
      command: <required>
      expectedStatus: <optional>
```
