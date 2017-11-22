# Sources

* src home: apisvc
* entrypoints:
  * `__main__.py`
  * `main.py`
  * `main_dev.py`
* chain of responsibility:
  * `__init__.py`
    * initiate object `app`
    * configure `app.config`
    * configure `app.logger`
    * import package `routes`
  * `routes/__init__.py`
    * import package `routes.v1`
  * `routes/v1/__init__.py`
    * import package `routes.v1.admin`, which will trigger url registration
    * import package `routes.v1.tenant`, which will trigger url registration
    * import package `routes.v1.user`, which will trigger url registration
  * `routes/v1/admin/__init__.py`
    * import object `ROUTE`
    * import module `routes.v1.admin.tenants`, which will trigger url registration
    * import module `routes.v1.admin.users`, which will trigger url registration
    * import module `routes.v1.admin.nodes`, which will trigger url registration
  * `routes/v1/admin/tenants.py`
    * import object `ROUTE`
  * `routes/v1/admin/users.py`
    * import object `ROUTE`
  * `routes/v1/admin/nodes.py`
    * import object `ROUTE`
  * `routes/v1/tenant/__init__.py`
    * import object `ROUTE`
    * import module `routes.v1.tenant.vms`, which will trigger url registration
    * import module `routes.v1.tenant.pods`, which will trigger url registration
  * `routes/v1/user/__init__.py`
    * import object `ROUTE`
    * import module `routes.v1.user.vms`, which will trigger url registration
    * import module `routes.v1.user.pods`, which will trigger url registration
  * `__main__.py`
    * import object `app`
    * invoke method `app.run()`
  * `main.py`
    * import object `app`
    * invoke method `app.run()`

---

More about package `common`

* `__init__.py`
  * import object `app` then expose as `APP`
* `config.py`
  * import object `APP` then expose its `config` as `CONFIG`
* `log.py`
  * import object `APP` then expose its `logger` as `LOGGER`
* `route.py`
  * import object `APP` then expose its `route` as `ROUTE`
* `profile.py`
  * import object `LOGGER`
* `util.py`
  * import object `CONFIG`
* `check.py`
  * import object `LOGGER`
  * import object `CONFIG`

---

More about `routes/v1/admin/__init__.py`

* import and invoke function `common.profile.timeit`

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

More about `routes/v1/tenant/__init__.py`

* import and invoke function `common.check.need_personate_header`
* function `common.check.need_personate_header`
  * invoke function `flask.request.headers.get`
  * invoke function `flask.abort`
  * inject object `apisvc_res_manager`

Same applied to

* `routes/v1/admin/tenants.py`
* `routes/v1/admin/users.py`
* `routes/v1/admin/nodes.py`
* `routes/v1/tenant/vms.py`
* `routes/v1/tenant/pods.py`
* `routes/v1/user/vms.py`
* `routes/v1/user/pods.py`

---

More about relations among packages `routes`, `responses`, `handlers`

2 Types of routes:

1. If the returned message is plain text, no corresponding response and handler objects.
2. If the returned message is of JSON format,
  * message keys are specified in the corresponding response object
  * message values are updated by the corresponding handler object