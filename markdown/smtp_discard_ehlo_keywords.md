# smtp_discard_ehlo_keywords (default: empty)
 A case insensitive list of EHLO keywords (pipelining, starttls,
auth, etc.) that the Postfix SMTP client will ignore in the EHLO
response from a remote SMTP server. 


 This feature is available in Postfix 2.2 and later. 


 Notes: 


* Specify the **silent-discard** pseudo keyword to prevent
this action from being logged.
* Use the smtp\_discard\_ehlo\_keyword\_address\_maps feature to
discard EHLO keywords selectively.


