# unverified_recipient_tempfail_action (default: $reject_tempfail_action)
 The Postfix SMTP server's action when reject\_unverified\_recipient
fails due to a temporary error condition. Specify "defer" to defer
the remote SMTP client request immediately. With the default
"defer\_if\_permit" action, the Postfix SMTP server continues to look
for opportunities to reject mail, and defers the client request
only if it would otherwise be accepted. 


 This feature is available in Postfix 2.6 and later. 


