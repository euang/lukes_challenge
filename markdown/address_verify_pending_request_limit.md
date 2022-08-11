# address_verify_pending_request_limit (default: see "postconf -d" output)
 A safety limit that prevents address verification requests from
overwhelming the Postfix queue. By default, the number of pending
requests is limited to 1/4 of the active queue maximum size
(qmgr\_message\_active\_limit). The queue manager enforces the limit
by tempfailing requests that exceed the limit. This affects only
unknown addresses and inactive addresses that have expired, because
the verify(8) daemon automatically refreshes an active address
before it expires. 


 This feature is available in Postfix 3.1 and later. 


