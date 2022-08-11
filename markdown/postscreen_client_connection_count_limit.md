# postscreen_client_connection_count_limit (default: $smtpd_client_connection_count_limit)
 How many simultaneous connections any remote SMTP client is
allowed to have
with the postscreen(8) daemon. By default, this limit is the same
as with the Postfix SMTP server. Note that the triage process can
take several seconds, with the time spent in postscreen\_greet\_wait
delay, and with the time spent talking to the postscreen(8) built-in
dummy SMTP protocol engine. 


 This feature is available in Postfix 2.8. 


