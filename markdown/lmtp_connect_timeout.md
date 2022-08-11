# lmtp_connect_timeout (default: 0s)
 The Postfix LMTP client time limit for completing a TCP connection, or
zero (use the operating system built-in time limit). When no
connection can be made within the deadline, the LMTP client tries
the next address on the mail exchanger list. 


 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



Example:




```

lmtp\_connect\_timeout = 30s

```

