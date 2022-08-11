# smtpd_timeout (default: normal: 300s, overload: 10s)
 When the Postfix SMTP server wants to send an SMTP server
response, how long the Postfix SMTP server will wait for an underlying
network write operation to complete; and when the Postfix SMTP
server Postfix wants to receive an SMTP client request, how long
the Postfix SMTP server will wait for an underlying network read
operation to complete. See the smtpd\_per\_request\_deadline for how
this time limit may be enforced (with Postfix 2.9-3.6 see
smtpd\_per\_record\_deadline). 


 Normally the default limit
is 300s, but it changes under overload to just 10s. With Postfix
2.5 and earlier, the SMTP server always uses a time limit of 300s
by default.




Note: if you set SMTP time limits to very large values you may have
to update the global ipc\_timeout parameter.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


