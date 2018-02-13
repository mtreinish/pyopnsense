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

# All the successful HTTP status codes from RFC 7231 & 4918
HTTP_SUCCESS = (200, 201, 202, 203, 204, 205, 206, 207)


class OPNClient(object):

    def __init__(self, api_key, api_secret, base_url, verify_cert=False):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.verify_cert = verify_cert

    def _process_response(self, response):
        if response.status_code in HTTP_SUCCESS:
            return json.loads(response.text)
        else:
            raise exceptions.APIException(status_code=response.status_code,
                                          resp_body=response.text)

    def _get(self, url):
        req_url = self.base_url + '/' + url
        response = requests.get(req_url, verify=self.verify_cert,
                                auth=(self.api_key, self.api_secret))
        return self._process_response(response)

    def _head(self, url):
        req_url = self.base_url + '/' + url
        response = requests.head(req_url, verify=self.verify_cert,
                                 auth=(self.api_key, self.api_secret))
        return self._process_response(response)

    def _post(self, url, body):
        req_url = self.base_url + '/' + url
        response = requests.post(req_url, data=body, verify=self.verify_cert,
                                 auth=(self.api_key, self.api_secret))
        return self._process_response(response)

    def _put(self, url, body):
        req_url = self.base_url + '/' + url
        response = requests.put(req_url, data=body, verify=self.verify_cert,
                                auth=(self.api_key, self.api_secret))
        return self._process_response(response)

    def _delete(self, url):
        req_url = self.base_url + '/' + url
        response = requests.delete(req_url, verify=self.verify_cert,
                                   auth=(self.api_key, self.api_secret))
        return self._process_response(response)

    def _patch(self, url, body):
        req_url = self.base_url + '/' + url
        response = requests.patch(req_url, data=body, verify=self.verify_cert,
                                  auth=(self.api_key, self.api_secret))
        return self._process_response(response)
