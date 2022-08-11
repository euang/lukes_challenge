# smtp_pix_workaround_delay_time (default: 10s)

How long the Postfix SMTP client pauses before sending
".<CR><LF>" in order to work around the PIX firewall
"<CR><LF>.<CR><LF>" bug.




Choosing too short a time makes this workaround ineffective when
sending large messages over slow network connections.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


