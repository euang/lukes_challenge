# qmgr_message_recipient_minimum (default: 10)

The minimal number of in-memory recipients for any message. This
takes priority over any other in-memory recipient limits (i.e.,
the global qmgr\_message\_recipient\_limit and the per transport
\_recipient\_limit) if necessary. The minimum value allowed for this
parameter is 1.



