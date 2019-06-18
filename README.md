# DGR

A project built using Django + GraphQL + React.

## Getting Started

```bash
cd dgr

# Setup Virtual Environment
python3 -m venv ./dgr/venv
source ./venv/bin/activate

# Intall Requirements
pip install -r requirements.txt

# Migrate Database
python3 manage.py migrate

# Load Fixtures
python3 manage.py loaddata cocktails
```

## Commands

### Development

- Env: `source ./venv/bin/activate`
- Start Server: `python3 manage.py runserver`

### Dependencies

- Install: `pip install -r requirements.txt`
- Freeze: `pip freeze > requirements.txt`
