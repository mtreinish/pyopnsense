from pyopnsense import client


class FirewallClient(client.OPNClient):
    """A client for interacting with the firewall endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def get_automation_rules(self):
        """Return the current firewall automation rules.

        :returns: A dict representing the current firewall rules
        :rtype: dict
        """
        return self._get("firewall/filter/searchRule")

    def get_rule_status(self, uuid):
        """
        Return the current status (enabled/disabled) of a specific firewall rule

        Parameter:  uuid

        :returns: A dict representing the current state of a firewall rule
        :rtype: dict
        """

        return self._get(f"firewall/filter/getRule/{uuid}")

    def toggle_rule(self, uuid):
        """
        Function to toggle a specific rule by uuid

        :returns: A dict representing the new status of the rule
        :rtype: dict
        """
        return self._post(f"firewall/filter/toggleRule/{uuid}", "")

    def apply_rules(self):
        """
        Function to apply changes to rules.

        """
        self._post(f"firewall/filter/apply/", "")
