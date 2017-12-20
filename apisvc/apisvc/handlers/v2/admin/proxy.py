from apisvc.common.log import LOGGER
from flask import abort


class Proxy(object):

    def put(self, manager, in_message, out_message, cmd, *args, **kwargs):
        # process in_message
        arg = in_message['arg']

        # delegate to manager
        data, error = manager.proxy(cmd=cmd, arg=arg)

        # process result
        if error is None:
            # update out_message
            LOGGER.debug('out_message: {0}'.format(out_message))
            out_message.update(data)
            LOGGER.debug('out_message: {0}'.format(out_message))
            return out_message, {'Content-Type': 'application/json'}
        else:
            LOGGER.warn('aborting bad response due to internal server error')
            return error, 500, {'Content-Type': 'application/json'}


def new_handler():
    return Proxy()
