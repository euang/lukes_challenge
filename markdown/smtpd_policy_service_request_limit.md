# smtpd_policy_service_request_limit (default: 0)

The maximal number of requests per SMTPD policy service connection,
or zero (no limit). Once a connection reaches this limit, the
connection is closed and the next request will be sent over a new
connection. This is a workaround to avoid error-recovery delays
with policy servers that cannot maintain a persistent connection.




This feature is available in Postfix 3.0 and later.



