==========
pyopnsense
==========
A python API client for the OPNsense API. This provides a python interface for
interacting with the OPNsense API.


Installation
============
pyopnsense is available via pypi so all you need to do is run::

   pip install -U pyopnsense

to get the latest pyopnsense release on your system. If you need to use a
development version of pyopnsense you can clone the repo and install it locally
with::

  git clone https://github.com/mtreinish/pyopnsense && pip install -e pyopnsense

which will install pyopnsense in your python environment in editable mode for
development.

Usage
=====

To use pyopnsense you need a couple pieces of information, the API key and the
API secret. Both can be created/found from the OPNsense web UI by navigating
to: `System->Access->Users` under `API keys`.

More information on this can be found in the OPNsense documentation:
https://docs.opnsense.org/development/how-tos/api.html

Once you have the API key and API secret you can use pyopnsense to interact
with your OPNsense installation. You can do this by passing your credentials
to a client class. For example::

    from pyopnsense import diagnostics

    api_key = XXXXXX
    api_secret = XXXXXXXXXXXXXXX
    opnsense_url = http://192.168.1.1/api'

    netinsight_client = diagnostics.NetworkInsightClient(api_key, api_secret,
                                                         base_url)
    print(netinsight_client.get_interfaces())

which will print a dictionary mapping physical devices to their interface label.

This same formula can be used to access each individual API endpoint you need
to access. The basic structure of the library is setup to roughly mirror the
endpoint tree of the OPNsense API. Each client module maps to the base endpoint
and then there is a client class in those modules for the next level up off
that.
