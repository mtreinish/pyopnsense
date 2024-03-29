API Reference
=============

This document attempts to document the API provided by the pyopnsense library.
It is a combination of autogenerated API documentation and usage explanations.

Instantiating Clients
---------------------

All the firmware client classes are based off the base OPNClient class and
are instantiated the same way. They require the same 3 mandatory arguments
the ``api_key``, the ``api_secret``, and the ``base_url``. With these 3 pieces
of information you can instantiate any of the client classes. The :ref:`usage`
section of the README contains details on how to get the ``api_key`` and
``api_secret`` values. The ``base_url`` is the base api endpoint for your
OPNsense installtion and is normally just http://$OPNsenseAddress/api
where ``$OPNsenseAddress`` is the hostname or IP address of your OPNsense
installation.

SSL Certificate Verification
''''''''''''''''''''''''''''

By default the SSL certificate verification is disabled. This is to enable a
working client out of the box, since by default OPNsense is its own CA, so
it likely won't be in your system's CA bundle. The tradeoff here is obviously
security. It's **strongly** recommended that you enable SSL verification once
you start using the client for anything beyond basic testing. To do this the
``verify_cert`` kwarg is used. This value gets passed directly to `requests`_
``verify`` kwarg on the HTTP methods. You can set this to either ``True`` which
will enable it and use your default system installed CA bundles, or the path to
a CA certificate or bundle directory. More details can be found in the `requests
documentation`_.

.. _requests: http://docs.python-requests.org/en/master/
.. _requests documentation: http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification

Client Classes
==============

Firmware API
------------
.. automodule:: pyopnsense.firmware
    :members:
    :show-inheritance:

Diagnostics API
---------------
.. automodule:: pyopnsense.diagnostics
    :members:
    :show-inheritance:

Routes API
---------------
.. automodule:: pyopnsense.routes
    :members:
    :show-inheritance:
