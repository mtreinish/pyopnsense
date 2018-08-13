# Copyright 2018 Matthew Treinish
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

import json

from pyopnsense import client


class FirmwareClient(client.OPNClient):
    """A client for interacting with the core/firmware endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def status(self):
        """Return the current firmware update status.

        :returns: A dict representing the current upgrade status for the
                  OPNsense firmware.
        :rtype: dict
        """
        return self._get('core/firmware/status')

    def upgrade(self, upgrade_list=None):
        """Issue an upgrade request.

        :param list upgrade_list: The list of packages to upgrade. If none are
            specified it will issue a request to upgrade all packages.
        """
        if upgrade_list is None:
            upgrade_list = 'all'
        body = json.dumps({'upgrade': upgrade_list})
        return self._post('core/firmware/upgrade', body)
