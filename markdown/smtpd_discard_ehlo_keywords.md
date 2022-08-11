# smtpd_discard_ehlo_keywords (default: empty)
 A case insensitive list of EHLO keywords (pipelining, starttls,
auth, etc.) that the Postfix SMTP server will not send in the EHLO
response
to a remote SMTP client. 


 This feature is available in Postfix 2.2 and later. 


 Notes: 


* Specify the **silent-discard** pseudo keyword to prevent
this action from being logged.
* Use the smtpd\_discard\_ehlo\_keyword\_address\_maps feature
to discard EHLO keywords selectively.


