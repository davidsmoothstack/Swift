# Package Management System

## Prerequisites

- Python 3 installed

## How to use

- Add desired packages into `packages.yml` with this format:

```yml
packages:
  - name: <string>
    manager:
      name: (apt|snap|yum)
    postInstallTest:
      command: <string>

  - name: openssh-client
    manager:
      name: apt
    postInstallTest:
      command: ""
```

- Execute main.py with
  - `$ ./main.py`
  - `python3 main.py`
