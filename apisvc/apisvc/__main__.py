from apisvc import app

if __name__ == "__main__":
    import logging
    app.logger.setLevel(logging.WARNING)

    from logging.handlers import RotatingFileHandler
    handler = RotatingFileHandler('/tmp/apisvc.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    app.run()
