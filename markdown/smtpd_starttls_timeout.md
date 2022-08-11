# smtpd_starttls_timeout (default: see "postconf -d" output)
 The time limit for Postfix SMTP server write and read operations
during TLS startup and shutdown handshake procedures. The current
default value is stress-dependent. Before Postfix version 2.8, it
was fixed at 300s. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.2 and later. 


