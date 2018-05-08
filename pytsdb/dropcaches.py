from pytsdb import request


def dropcaches(host, port, protocol):
    """

    :param host: str
    :param port: str
    :param protocol: str
    :return: json
    """
    url = api_url(host, port, protocol)
    return request.generic_request(url)


def api_url(host, port, protocol):
    """
    Make api url to obtain configuration

    :param host: str
    :param port: str
    :param protocol: str
    :return: str
    """
    return '{}://{}:{}/api/dropcaches/'.format(protocol, host, port)