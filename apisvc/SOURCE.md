# Sources

* src home: apisvc
* entrypoints:
  * `__main__.py`
  * `main.py`
  * `main_dev.py`
* chain of responsibility:
  * `__init__.py`
    * initiate object `app`
    * import package `routes`
  * `routes/__init__.py`
    * import package `routes.v1`
  * `routes/v1/__init__.py`
    * import package `routes.v1.admin`, which will trigger url registration
    * import package `routes.v1.tenant`, which will trigger url registration
    * import package `routes.v1.user`, which will trigger url registration
  * `routes/v1/admin/__init__.py`
    * import object `app`
    * invoke method `app.route()`
    * import module `routes.v1.admin.tenants`, which will trigger url registration
    * import module `routes.v1.admin.users`, which will trigger url registration
    * import module `routes.v1.admin.nodes`, which will trigger url registration
  * `routes/v1/admin/tenants.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/admin/users.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/admin/nodes.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/tenant/__init__.py`
    * import object `app`
    * invoke method `app.route()`
    * import module `routes.v1.tenant.vms`, which will trigger url registration
    * import module `routes.v1.tenant.pods`, which will trigger url registration
  * `routes/v1/user/__init__.py`
    * import object `app`
    * invoke method `app.route()`
    * import module `routes.v1.user.vms`, which will trigger url registration
    * import module `routes.v1.user.pods`, which will trigger url registration
  * `__main__.py`
    * import object `app`
    * configure `app.logger`
    * invoke method `app.run()`
  * `main.py`
    * import object `app`
    * configure `app.logger`
    * invoke method `app.run()`

---

More about `routes/v1/admin/__init__.py`

* import and invoke function `common.timeit.timeit`
* function `common.timeit.timeit`
  * import object `app`
  * invoke function `app.logger.debug`

Same applied to

* `routes/v1/admin/tenants.py`
* `routes/v1/admin/users.py`
* `routes/v1/admin/nodes.py`
* `routes/v1/tenant/__init__.py`
* `routes/v1/tenant/vms.py`
* `routes/v1/tenant/pods.py`
* `routes/v1/user/__init__.py`
* `routes/v1/user/vms.py`
* `routes/v1/user/pods.py`

---
