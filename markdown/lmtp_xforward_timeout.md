# lmtp_xforward_timeout (default: 300s)

The Postfix LMTP client time limit for sending the XFORWARD command,
and for receiving the remote LMTP server response.




In case of problems the client does NOT try the next address on
the mail exchanger list.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



This feature is available in Postfix 2.1 and later.



