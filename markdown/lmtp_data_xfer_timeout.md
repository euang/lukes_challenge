# lmtp_data_xfer_timeout (default: 180s)

The Postfix LMTP client time limit for sending the LMTP message
content.
When the connection stalls for more than $lmtp\_data\_xfer\_timeout
the LMTP client terminates the transfer.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


