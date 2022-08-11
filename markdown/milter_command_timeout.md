# milter_command_timeout (default: 30s)
 The time limit for sending an SMTP command to a Milter (mail
filter) application, and for receiving the response. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.3 and later. 


