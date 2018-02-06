

from pyopnsense import client

class FirmwareClient(client.OPNClient):

    def status(self):
        return self._get('core/firmware/status')
