# smtp_pix_workaround_threshold_time (default: 500s)
 How long a message must be queued before the Postfix SMTP client
turns on the PIX firewall "<CR><LF>.<CR><LF>"
bug workaround for delivery through firewalls with "smtp fixup"
mode turned on. 


 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



By default, the workaround is turned off for mail that is queued
for less than 500 seconds. In other words, the workaround is normally
turned off for the first delivery attempt.




Specify 0 to enable the PIX firewall
"<CR><LF>.<CR><LF>" bug workaround upon the
first delivery attempt.



