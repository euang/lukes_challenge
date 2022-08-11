# postscreen_discard_ehlo_keyword_address_maps (default: $smtpd_discard_ehlo_keyword_address_maps)
 Lookup tables, indexed by the remote SMTP client address, with
case insensitive lists of EHLO keywords (pipelining, starttls, auth,
etc.) that the postscreen(8) server will not send in the EHLO response
to a remote SMTP client. See smtpd\_discard\_ehlo\_keywords for details.
The table is not searched by hostname for robustness reasons. 


 This feature is available in Postfix 2.8 and later. 


