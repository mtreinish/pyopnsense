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

    def status(self):
        return self._get('diagnostics/netflow/status')


class InterfaceClient(client.OPNClient):

    def get_ndp(self):
        return self._get('diagnostics/interface/getNdp')

    def get_arp(self):
        return self._get('diagnostics/interface/getArp')


class NetworkInsightClient(client.OPNClient):

    def get_interfaces(self):
        return self._get('diagnostics/networkinsight/getinterfaces')

    def get_services(self):
        return self._get('diagnostics/networkinsight/getservices')

    def get_protocols(self):
        return self._get('diagnostics/networkinsight/getprotocols')

    def get_timeserie(self):
        return self._get('diagnostics/networkinsight/timeserie')


class SystemHealthClient(client.OPNClient):

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
