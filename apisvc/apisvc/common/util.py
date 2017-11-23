from apisvc.common.config import CONFIG


def personation_to_role_account(personation):
    return tuple(personation.split(' '))
