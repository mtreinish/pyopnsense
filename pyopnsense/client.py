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


class OPNClient(object):

    def __init__(self, api_key, api_secret, base_url, verify_cert=False):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.verify_cert = verify_cert

    def _get(self, url):
        req_url = self.base_url + '/' + url
        response = requests.get(req_url, verify=self.verify_cert,
                               auth=(self.api_key, self.api_secret))
        if response.status_code == 200:
            print response.text
            return json.loads(response.text)
        else:
            raise exceptions.APIException(status_code=response.status_code,
                                          resp_body=response.text)
