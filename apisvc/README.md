# Versions

* python: 2.7.11
* others: see requirements.txt

# Sources

* src home: apisvc
* entrypoint: main.py

# Setup Development Environment

```
git clone ...
cd ...
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Start development server (single thread)

```
cd apisvc
python main.py
``` 

Start development server (two threads)

```
cd apisvc
gunicorn --workers=2 -b 127.0.0.1:5000 main:app
``` 

# Usage


