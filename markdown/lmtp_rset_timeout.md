# lmtp_rset_timeout (default: 20s)
 The Postfix LMTP client time limit for sending the RSET command,
and for receiving the remote LMTP server response. The LMTP client
sends RSET in
order to finish a recipient address probe, or to verify that a
cached connection is still alive. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


