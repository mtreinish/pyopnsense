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

from six.moves import urllib

from pyopnsense import client


class NetFlowClient(client.OPNClient):
    """A client for interacting with the diagnostics/netflow endpoint

    :param str api_key: The api key to use for requests
    :param str api_secret: The api secret to use for requests
    :param str base_url: THe base api endpoint for the OPNsense deployment
    """
    def status(self):
        """Return the current netflow status

        :returns: A dict representing the current status of netflow
        :rtype: dict
        """
        return self._get('diagnostics/netflow/status')


class InterfaceClient(client.OPNClient):
    """A client for interacting with the diagnostics/interface endpoint

    :param str api_key: The api key to use for requests
    :param str api_secret: The api secret to use for requests
    :param str base_url: THe base api endpoint for the OPNsense deployment
    """
    def get_ndp(self):
        """Get NDP table for router"""
        return self._get('diagnostics/interface/getNdp')

    def get_arp(self):
        """Get ARP table for router"""
        return self._get('diagnostics/interface/getArp')


class NetworkInsightClient(client.OPNClient):
    """A client for interacting with the diagnostics/networkinsight endpoint

    :param str api_key: The api key to use for requests
    :param str api_secret: The api secret to use for requests
    :param str base_url: THe base api endpoint for the OPNsense deployment
    """
    def get_interfaces(self):
        return self._get('diagnostics/networkinsight/getinterfaces')

    def get_services(self):
        return self._get('diagnostics/networkinsight/getservices')

    def get_protocols(self):
        return self._get('diagnostics/networkinsight/getprotocols')

    def get_timeserie(self):
        return self._get('diagnostics/networkinsight/timeserie')


class SystemHealthClient(client.OPNClient):
    """A client for interacting with the diagnostics/systemhealth endpoint

    :param str api_key: The api key to use for requests
    :param str api_secret: The api secret to use for requests
    :param str base_url: THe base api endpoint for the OPNsense deployment
    """
    def get_health_list(self):
        return self._get('diagnostics/systemhealth/getRRDlist')

    def get_health_data(self, metric, start=0, stop=0, maxitems=1024,
                        inverse=False, details=False):
        url = ['diagnostics/systemhealth/getSystemHealth']
        url.append(urllib.parse.quote(metric))
        url.append(start)
        url.append(stop)
        url.append(maxitems)
        if inverse:
            url.append('true')
        else:
            url.append('false')
        if details:
            url.append('true')
        else:
            url.append('false')

        return self._get('/'.join(url))
