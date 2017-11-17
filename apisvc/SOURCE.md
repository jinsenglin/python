# Sources

* src home: apisvc
* entrypoints:
  * main.py
  * main_dev.py
* chain of responsibility:
  * `__init__.py`
    * initiate object `app`
    * import package `routes`
  * `routes/__init__.py`
    * import package `routes.v1`
  * `routes/v1/__init__.py`
    * import package `routes.v1.admin`, which will trigger url registration
    * import module `routes.v1.tenant`, which will trigger url registration
    * import module `routes.v1.user`, which will trigger url registration
  * `routes/v1/admin/__init__.py`
    * import object `app`
    * invoke method `app.route()`
    * import module `tenants`, which will trigger url registration
    * import module `nodes`, which will trigger url registration
  * `routes/v1/admin/tenants.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/admin/nodes.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/tenant.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/user.py`
    * import object `app`
    * invoke method `app.route()`
  * `main.py`
    * import object `app`
    * invoke method `app.run()`

