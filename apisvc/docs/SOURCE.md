# Source

* src home: apisvc
* entrypoints:
  * `__main__.py`
  * `main.py`
  * `main_dev.py`
* chain of responsibility:
  * `__main__.py`
    * import object `app`
    * invoke method `app.run()`
  * `__init__.py`
    * initiate object `app`
    * configure `app.config`
    * configure `app.logger`
    * import package `routes`
    * import package `resources`
  * `routes/__init__.py`
    * import package `v2`
    * import package `mock`
  * `resources/__init__.py`
    * import package `v2`
  * `resources/v2/__init__.py`
    * import package `admin`
    * import package `tenant`
    * import package `user`
  * `resources/v2/admin/__init__.py`
    * import package `nodes`
    * import package `pools`
    * import package `rings`
  * `resources/v2/admin/nodes/__init__.py`
    * import package `node`
  * `resources/v2/admin/nodes/node.py`
    * import object 'flask_restful.Resource'
    * invoke method 'flask_restful.Resource.add_resource()' # i.e. url registration

---

```
1 gm       /---------------/
2 cache   /---------------/

1 gm       /---------------/
2 shellm  /---------------/
3 shell  /---------------/
4 .sh   /---------------/

1 gm       /---------------/
2 dbm     /---------------/
3 db     /---------------/
```