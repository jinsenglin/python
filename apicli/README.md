# Usage

```
# PROJECT_HOME=.

cd $PROJECT_HOME
python -m apicli -h
```

```
# PROJECT_HOME=.

cd $PROJECT_HOME
python apicli/main.py -h
```

# Example

```
alias apicli="python -m apicli"

apicli openstack "project list"
apicli kubectl "get ns"
```