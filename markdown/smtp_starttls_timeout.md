# smtp_starttls_timeout (default: 300s)
 Time limit for Postfix SMTP client write and read operations
during TLS startup and shutdown handshake procedures. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.2 and later. 


