# Quickstart

```
# PROJECT_HOME = .

cd $PROJECT_HOME

pip install -r requirements.txt
pip install -r requirements-dev.txt

cd $PROJECT_HOME/scripts

bash check-bindep.sh # make sure all dependencies installed
bash bring-up-fresh-dev-env.sh FULL
```

# Setup PyCharm

see docs/PyCharm.md

# Test

see docs/TEST.md

# Debug

see docs/DEBUG.md

# Build source distribution tarball

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts
bash clear-fs-cache.sh

cd $PROJECT_HOME
python setup.py sdist --formats=gztar
```

# Go stage

see stage-site/README.md

# Source

* src home: apisvc
* entrypoints:
  * `__main__.py`
  * `main.py`
* chain of responsibility: see docs/SOURCE.md

# Dependency

see docs/DEPENDENCY.md

# Log

see docs/LOG.md

# Reference

see docs/REFERENCE.md
