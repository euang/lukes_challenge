# reject_tempfail_action (default: defer_if_permit)
 The Postfix SMTP server's action when a reject-type restriction
fails due to a temporary error condition. Specify "defer" to defer
the remote SMTP client request immediately. With the default
"defer\_if\_permit" action, the Postfix SMTP server continues to look
for opportunities to reject mail, and defers the client request
only if it would otherwise be accepted. 


 For finer control, see: unverified\_recipient\_tempfail\_action,
unverified\_sender\_tempfail\_action, unknown\_address\_tempfail\_action,
and unknown\_helo\_hostname\_tempfail\_action. 


 This feature is available in Postfix 2.6 and later. 


