# smtp_discard_ehlo_keyword_address_maps (default: empty)
 Lookup tables, indexed by the remote SMTP server address, with
case insensitive lists of EHLO keywords (pipelining, starttls, auth,
etc.) that the Postfix SMTP client will ignore in the EHLO response from a
remote SMTP server. See smtp\_discard\_ehlo\_keywords for details. The
table is not indexed by hostname for consistency with
smtpd\_discard\_ehlo\_keyword\_address\_maps. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 This feature is available in Postfix 2.2 and later. 


