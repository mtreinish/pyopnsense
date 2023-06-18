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

import requests

from pyopnsense import exceptions

DEFAULT_TIMEOUT = 5

# All the successful HTTP status codes from RFC 7231 & 4918
HTTP_SUCCESS = (200, 201, 202, 203, 204, 205, 206, 207)


class OPNClient(object):
    """Representation of the OPNsense API client."""

    def __init__(
        self, api_key, api_secret, base_url, verify_cert=False, timeout=DEFAULT_TIMEOUT
    ):
        """Initialize the OPNsense API client."""
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.verify_cert = verify_cert
        self.timeout = timeout

    def _process_response(self, response, raw=False):
        """Handle the response."""
        if response.status_code in HTTP_SUCCESS:
            return response.text if raw else json.loads(response.text)
        else:
            raise exceptions.APIException(
                status_code=response.status_code, resp_body=response.text
            )

    def _get(self, endpoint, raw=False):
        req_url = "{}/{}".format(self.base_url, endpoint)
        response = requests.get(
            req_url,
            verify=self.verify_cert,
            auth=(self.api_key, self.api_secret),
            timeout=self.timeout,
        )
        return self._process_response(response, raw)

    def _post(self, endpoint, body, raw=False):
        req_url = "{}/{}".format(self.base_url, endpoint)
        response = requests.post(
            req_url,
            data=body,
            verify=self.verify_cert,
            auth=(self.api_key, self.api_secret),
            timeout=self.timeout,
        )
        return self._process_response(response, raw)
