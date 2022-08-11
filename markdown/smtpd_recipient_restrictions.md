# smtpd_recipient_restrictions (default: see "postconf -d" output)

Optional restrictions that the Postfix SMTP server applies in the
context of a client RCPT TO command, after smtpd\_relay\_restrictions.
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
Restrictions are applied in the order as specified; the first
restriction that matches wins.




The following restrictions are specific to the recipient address
that is received with the RCPT TO command.




**check\_recipient\_access *type:table***
Search the specified access(5) database for the resolved RCPT
TO address, domain, parent domains, or localpart@, and execute the
corresponding action. 
**check\_recipient\_a\_access *type:table***
Search the specified access(5) database for the IP addresses for
the RCPT TO domain, and execute the corresponding action. Note:
a result of "OK" is not allowed for safety reasons. Instead, use
DUNNO in order to exclude specific hosts from denylists. This
feature is available in Postfix 3.0 and later. 
**check\_recipient\_mx\_access *type:table***
Search the specified access(5) database for the MX hosts for
the RCPT TO domain, and execute the corresponding action. If no
MX record is found, look up A or AAAA records, just like the Postfix
SMTP client would. Note:
a result of "OK" is not allowed for safety reasons. Instead, use
DUNNO in order to exclude specific hosts from denylists. This
feature is available in Postfix 2.1 and later. 
**check\_recipient\_ns\_access *type:table***
Search the specified access(5) database for the DNS servers
for the RCPT TO domain, and execute the corresponding action.
Note: a result of "OK" is not allowed for safety reasons. Instead,
use DUNNO in order to exclude specific hosts from denylists. This
feature is available in Postfix 2.1 and later. 
**permit\_auth\_destination**
Permit the request when one of the following is true:

* Postfix is a mail forwarder: the resolved RCPT TO domain matches
$relay\_domains or a subdomain thereof, and the address contains no
sender-specified routing (user@elsewhere@domain),
* Postfix is the final destination: the resolved RCPT TO domain
matches $mydestination, $inet\_interfaces, $proxy\_interfaces,
$virtual\_alias\_domains, or $virtual\_mailbox\_domains, and the address
contains no sender-specified routing (user@elsewhere@domain).

**permit\_mx\_backup**
Permit the request when the local mail system is a backup MX for
the RCPT TO domain, or when the domain is an authorized destination
(see permit\_auth\_destination for definition).

* Safety: permit\_mx\_backup does not accept addresses that have
sender-specified routing information (example: user@elsewhere@domain).
* Safety: permit\_mx\_backup can be vulnerable to mis-use when
access is not restricted with permit\_mx\_backup\_networks.
* Safety: as of Postfix version 2.3, permit\_mx\_backup no longer
accepts the address when the local mail system is a primary MX for
the recipient domain. Exception: permit\_mx\_backup accepts the address
when it specifies an authorized destination (see permit\_auth\_destination
for definition).
* Limitation: mail may be rejected in case of a temporary DNS
lookup problem with Postfix prior to version 2.0.

**reject\_non\_fqdn\_recipient**
Reject the request when the RCPT TO address specifies a
domain that is not in
fully-qualified domain form, as required by the RFC.   
 The
non\_fqdn\_reject\_code parameter specifies the response code for
rejected requests (default: 504). 
**reject\_rhsbl\_recipient *rbl\_domain=d.d.d.d***
Reject the request when the RCPT TO domain is listed with the
A record "*d.d.d.d*" under *rbl\_domain* (Postfix version
2.1 and later only). Each "*d*" is a number, or a pattern
inside "[]" that contains one or more ";"-separated numbers or
number..number ranges (Postfix version 2.8 and later). If no
"*=d.d.d.d*" is specified, reject
the request when the RCPT TO domain is listed with
any A record under *rbl\_domain*.   
 The maps\_rbl\_reject\_code
parameter specifies the response code for rejected requests (default:
554); the default\_rbl\_reply parameter specifies the default server
reply; and the rbl\_reply\_maps parameter specifies tables with server
replies indexed by *rbl\_domain*. This feature is available
in Postfix version 2.0 and later.
**reject\_unauth\_destination**
Reject the request unless one of the following is true:

* Postfix is a mail forwarder: the resolved RCPT TO domain matches
$relay\_domains or a subdomain thereof, and contains no sender-specified
routing (user@elsewhere@domain),
* Postfix is the final destination: the resolved RCPT TO domain
matches $mydestination, $inet\_interfaces, $proxy\_interfaces,
$virtual\_alias\_domains, or $virtual\_mailbox\_domains, and contains
no sender-specified routing (user@elsewhere@domain).

The relay\_domains\_reject\_code parameter specifies the response
code for rejected requests (default: 554). 
**defer\_unauth\_destination**
 Reject the same requests as reject\_unauth\_destination, with a
non-permanent error code. This feature is available in Postfix
2.10 and later.
**reject\_unknown\_recipient\_domain**
Reject the request when Postfix is not final destination for
the recipient domain, and the RCPT TO domain has 1) no DNS MX and
no DNS A
record or 2) a malformed MX record such as a record with
a zero-length MX hostname (Postfix version 2.3 and later).   
 The
reply is specified with the unknown\_address\_reject\_code parameter
(default: 450), unknown\_address\_tempfail\_action (default:
defer\_if\_permit), or 556 (nullmx, Postfix 3.0 and
later). See the respective parameter descriptions for details.

**reject\_unlisted\_recipient** (with Postfix version 2.0: check\_recipient\_maps)
 Reject the request when the RCPT TO address is not listed in
the list of valid recipients for its domain class. See the
smtpd\_reject\_unlisted\_recipient parameter description for details.
This feature is available in Postfix 2.1 and later.
**reject\_unverified\_recipient**
Reject the request when mail to the RCPT TO address is known
to bounce, or when the recipient address destination is not reachable.
Address verification information is managed by the verify(8) server;
see the ADDRESS\_VERIFICATION\_README file for details.   
 The
unverified\_recipient\_reject\_code parameter specifies the numerical
response code when an address is known to bounce (default: 450,
change it to 550 when you are confident that it is safe to do so).
  
The unverified\_recipient\_defer\_code parameter specifies the
numerical response code when an address probe failed due to a
temporary problem (default: 450).   
 The
unverified\_recipient\_tempfail\_action parameter specifies the action
after address probe failure due to a temporary problem (default:
defer\_if\_permit).   
 This feature breaks for aliased addresses
with "enable\_original\_recipient = no" (Postfix ≤ 3.2).   

This feature is available in Postfix 2.1 and later. 


Other restrictions that are valid in this context:



* Generic restrictions that can be used
in any SMTP command context, described under smtpd\_client\_restrictions.
* SMTP command specific restrictions described under
smtpd\_client\_restrictions, smtpd\_helo\_restrictions and
smtpd\_sender\_restrictions.



Example:




```

# The Postfix before 2.10 default mail relay policy. Later Postfix
# versions implement this preferably with smtpd\_relay\_restrictions.
smtpd\_recipient\_restrictions = permit\_mynetworks, reject\_unauth\_destination

```

