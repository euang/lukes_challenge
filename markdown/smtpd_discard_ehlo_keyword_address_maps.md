# smtpd_discard_ehlo_keyword_address_maps (default: empty)
 Lookup tables, indexed by the remote SMTP client address, with
case insensitive lists of EHLO keywords (pipelining, starttls, auth,
etc.) that the Postfix SMTP server will not send in the EHLO response
to a
remote SMTP client. See smtpd\_discard\_ehlo\_keywords for details.
The tables are not searched by hostname for robustness reasons. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 This feature is available in Postfix 2.2 and later. 


