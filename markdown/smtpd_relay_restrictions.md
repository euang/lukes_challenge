# smtpd_relay_restrictions (default: permit_mynetworks, permit_sasl_authenticated, defer_unauth_destination)
 Access restrictions for mail relay control that the Postfix
SMTP server applies in the context of the RCPT TO command, before
smtpd\_recipient\_restrictions.
See SMTPD\_ACCESS\_README, section "Delayed evaluation of SMTP access
restriction lists" for a discussion of evaluation context and time.



 With Postfix versions before 2.10, the rules for relay permission
and spam blocking were combined under smtpd\_recipient\_restrictions,
resulting in error-prone configuration. As of Postfix 2.10, relay
permission rules are preferably implemented with smtpd\_relay\_restrictions,
so that a permissive spam blocking policy under
smtpd\_recipient\_restrictions will no longer result in a permissive
mail relay policy. 


 For backwards compatibility, sites that migrate from Postfix
versions before 2.10 can set smtpd\_relay\_restrictions to the empty
value, and use smtpd\_recipient\_restrictions exactly as before. 



By default, the Postfix SMTP server accepts:



* Mail from clients whose IP address matches $mynetworks, or:
* Mail from clients who are SASL authenticated, or:
* Mail to remote destinations that match $relay\_domains, except
for addresses that contain sender-specified routing
(user@elsewhere@domain), or:
* Mail to local destinations that match $inet\_interfaces
or $proxy\_interfaces, $mydestination, $virtual\_alias\_domains, or
$virtual\_mailbox\_domains.



IMPORTANT: Either the smtpd\_relay\_restrictions or the
smtpd\_recipient\_restrictions parameter must specify
at least one of the following restrictions. Otherwise Postfix will
refuse to receive mail:




> 
> 
> ```
> 
> reject, reject\_unauth\_destination
> 
> ```
> 
> 



> 
> 
> ```
> 
> defer, defer\_if\_permit, defer\_unauth\_destination
> 
> ```
> 
> 



Specify a list of restrictions, separated by commas and/or whitespace.
Continue long lines by starting the next line with whitespace.
The same restrictions are available as documented under
smtpd\_recipient\_restrictions.



 This feature is available in Postix 2.10 and later. 


