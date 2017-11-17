from apisvc import app

if __name__ == "__main__":
    import logging
    app.logger.setLevel(logging.DEBUG) # WARNING for production, DEBUG for development

    from logging.handlers import RotatingFileHandler
    handler = RotatingFileHandler('/tmp/apisvc.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    app.run()
