from apisvc.common.log import LOGGER


class Proxy(object):

    def put(self, manager, in_message, out_message, cmd, *args, **kwargs):
        # process in_message
        arg = in_message['arg']

        # delegate to manager
        result = manager.proxy(cmd=cmd, arg=arg)

        # TODO may process result

        # update out_message
        LOGGER.debug('out_message: {0}'.format(out_message))
        out_message.update(result)
        LOGGER.debug('out_message: {0}'.format(out_message))

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Proxy()
