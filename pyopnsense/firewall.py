# Copyright 2022 Patrick Carr
#
# This file is part of pyopnsense
#
# pyopnsense is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyopnsense is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyopnsense. If not, see <http://www.gnu.org/licenses/>.

from pyopnsense import client


class FirewallClient(client.OPNClient):
    """A client for interacting with the firewall endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    :param int timeout: The timeout in seconds for API requests
    """

    def get_automation_rules(self):
        """Return the current firewall automation rules.

        :returns: A dict representing the current firewall rules
        :rtype: dict
        """
        return self._get("firewall/filter/searchRule")

    def get_rule_status(self, uuid):
        """Return the current status (enabled/disabled) of a specific firewall
        rule

        Parameter:  uuid

        :returns: A dict representing the current state of a firewall rule
        :rtype: dict
        """

        return self._get(f"firewall/filter/getRule/{uuid}")

    def toggle_rule(self, uuid):
        """Function to toggle a specific rule by uuid

        :returns: A dict representing the new status of the rule
        :rtype: dict
        """
        return self._post(f"firewall/filter/toggleRule/{uuid}", "")

    def apply_rules(self):
        """Function to apply changes to rules."""
        self._post("firewall/filter/apply/", "")
