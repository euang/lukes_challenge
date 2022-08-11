# smtp_data_xfer_timeout (default: 180s)

The Postfix SMTP client time limit for sending the SMTP message content.
When the connection makes no progress for more than $smtp\_data\_xfer\_timeout
seconds the Postfix SMTP client terminates the transfer.




Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds).



