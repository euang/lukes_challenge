# postscreen_discard_ehlo_keywords (default: $smtpd_discard_ehlo_keywords)
 A case insensitive list of EHLO keywords (pipelining, starttls,
auth, etc.) that the postscreen(8) server will not send in the EHLO
response to a remote SMTP client. See smtpd\_discard\_ehlo\_keywords
for details. 


 This feature is available in Postfix 2.8 and later. 


