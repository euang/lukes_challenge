# default_recipient_limit (default: 20000)

The default per-transport upper limit on the number of in-memory
recipients. These limits take priority over the global
qmgr\_message\_recipient\_limit after the message has been assigned
to the respective transports. See also default\_extra\_recipient\_limit
and qmgr\_message\_recipient\_minimum.



 Use *transport*\_recipient\_limit to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.



