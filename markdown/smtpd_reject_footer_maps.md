# smtpd_reject_footer_maps (default: empty)
 Lookup tables, indexed by the complete Postfix SMTP server 4xx or
5xx response, with reject footer templates. See smtpd\_reject\_footer
for details. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 This feature is available in Postfix 3.4 and later. 


