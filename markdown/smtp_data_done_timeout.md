# smtp_data_done_timeout (default: 600s)

The Postfix SMTP client time limit for sending the SMTP ".", and
for receiving the remote SMTP server response.




When no response is received within the deadline, a warning is
logged that the mail may be delivered multiple times.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


