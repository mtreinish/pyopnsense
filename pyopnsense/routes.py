from pyopnsense import client


class GatewayClient(client.OPNClient):
    """A client for interacting with the routes/gateway endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def status(self):
        """Return the current gateways status.

        :returns: A dict representing the current status of gateways
        :rtype: dict
        """
        return self._get('routes/gateway/status')
