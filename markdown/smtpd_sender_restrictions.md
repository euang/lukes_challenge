# smtpd_sender_restrictions (default: empty)

Optional restrictions that the Postfix SMTP server applies in the
context of a client MAIL FROM command.
See SMTPD\_ACCESS\_README, section "Delayed evaluation of SMTP access
restriction lists" for a discussion of evaluation context and time.




The default is to permit everything.




Specify a list of restrictions, separated by commas and/or whitespace.
Continue long lines by starting the next line with whitespace.
Restrictions are applied in the order as specified; the first
restriction that matches wins.




The following restrictions are specific to the sender address
received with the MAIL FROM command.




**check\_sender\_access *type:table***
Search the specified access(5) database for the MAIL FROM
address, domain, parent domains, or localpart@, and execute the
corresponding action. 
**check\_sender\_a\_access *type:table***
Search the specified access(5) database for the IP addresses for
the MAIL FROM domain, and execute the corresponding action. Note:
a result of "OK" is not allowed for safety reasons. Instead, use
DUNNO in order to exclude specific hosts from denylists. This
feature is available in Postfix 3.0 and later. 
**check\_sender\_mx\_access *type:table***
Search the specified access(5) database for the MX hosts for
the MAIL FROM domain, and execute the corresponding action. If no
MX record is found, look up A or AAAA records, just like the Postfix
SMTP client would. Note:
a result of "OK" is not allowed for safety reasons. Instead, use
DUNNO in order to exclude specific hosts from denylists. This
feature is available in Postfix 2.1 and later. 
**check\_sender\_ns\_access *type:table***
Search the specified access(5) database for the DNS servers
for the MAIL FROM domain, and execute the corresponding action.
Note: a result of "OK" is not allowed for safety reasons. Instead,
use DUNNO in order to exclude specific hosts from denylists. This
feature is available in Postfix 2.1 and later. 
**reject\_authenticated\_sender\_login\_mismatch**
 Reject the request when the client is authenticated with SASL,
but either the MAIL FROM address is not listed in $smtpd\_sender\_login\_maps,
or the SASL login name is not an owner for that address.
  

This prevents an authenticated client from using a MAIL FROM address
that they do not explicitly own.
  

This feature is available in Postfix version 2.1 and later. 
**reject\_known\_sender\_login\_mismatch**
 When the client is authenticated with SASL, reject the request
when the MAIL FROM address is listed in $smtpd\_sender\_login\_maps,
but the SASL login name is not an owner for that address.
  

When the client is not authenticated with SASL, reject the request
when SASL is enabled, and the MAIL FROM address is listed in
$smtpd\_sender\_login\_maps.
  

This protects any MAIL FROM address that is listed in
$smtpd\_sender\_login\_maps, while still allowing a client to use any
unlisted MAIL FROM address.
  

This feature is available in Postfix version 2.11 and later.
**reject\_non\_fqdn\_sender**
Reject the request when the MAIL FROM address specifies a
domain that is not in
fully-qualified domain form as required by the RFC.   
 The
non\_fqdn\_reject\_code parameter specifies the response code for
rejected requests (default: 504). 
**reject\_rhsbl\_sender *rbl\_domain=d.d.d.d***
Reject the request when the MAIL FROM domain is listed with
the A record "*d.d.d.d*" under *rbl\_domain* (Postfix
version 2.1 and later only). Each "*d*" is a number, or a
pattern inside "[]" that contains one or more ";"-separated numbers
or number..number ranges (Postfix version 2.8 and later). If no
"*=d.d.d.d*" is specified,
reject the request when the MAIL FROM domain is
listed with any A record under *rbl\_domain*.   
 The
maps\_rbl\_reject\_code parameter specifies the response code for
rejected requests (default: 554); the default\_rbl\_reply parameter
specifies the default server reply; and the rbl\_reply\_maps parameter
specifies tables with server replies indexed by *rbl\_domain*.
This feature is available in Postfix 2.0 and later.
**reject\_sender\_login\_mismatch**
 As of Postfix 2.1, this is an alias for
"reject\_authenticated\_sender\_login\_mismatch,
reject\_unauthenticated\_sender\_login\_mismatch".
**reject\_unauthenticated\_sender\_login\_mismatch**
 Reject the request when SASL is enabled, the MAIL FROM address
is listed in $smtpd\_sender\_login\_maps, but the client is not
authenticated with SASL.
  

With SASL enabled, this prevents an unauthenticated client from
using any MAIL FROM address that is listed in $smtpd\_sender\_login\_maps.
  

This feature is available in Postfix version 2.1 and later.
**reject\_unknown\_sender\_domain**
Reject the request when Postfix is not the final destination for
the sender address, and the MAIL FROM domain has 1) no DNS MX and
no DNS A
record, or 2) a malformed MX record such as a record with
a zero-length MX hostname (Postfix version 2.3 and later).   
 The
reply is specified with the unknown\_address\_reject\_code parameter
(default: 450), unknown\_address\_tempfail\_action (default:
defer\_if\_permit), or 550 (nullmx, Postfix 3.0 and
later). See the respective parameter descriptions for details.

**reject\_unlisted\_sender**
Reject the request when the MAIL FROM address is not listed in
the list of valid recipients for its domain class. See the
smtpd\_reject\_unlisted\_sender parameter description for details.
This feature is available in Postfix 2.1 and later.
**reject\_unverified\_sender**
Reject the request when mail to the MAIL FROM address is known to
bounce, or when the sender address destination is not reachable.
Address verification information is managed by the verify(8) server;
see the ADDRESS\_VERIFICATION\_README file for details.   
 The
unverified\_sender\_reject\_code parameter specifies the numerical
response code when an address is known to bounce (default: 450,
change into 550 when you are confident that it is safe to do so).
  
The unverified\_sender\_defer\_code specifies the numerical response
code when an address probe failed due to a temporary problem
(default: 450).   
 The unverified\_sender\_tempfail\_action parameter
specifies the action after address probe failure due to a temporary
problem (default: defer\_if\_permit).   
 This feature breaks for
aliased addresses with "enable\_original\_recipient = no" (Postfix
≤ 3.2).   
 This feature is available in Postfix 2.1 and later.



Other restrictions that are valid in this context:



* Generic restrictions that can be used
in any SMTP command context, described under smtpd\_client\_restrictions.
* SMTP command specific restrictions described under
smtpd\_client\_restrictions and smtpd\_helo\_restrictions.
* SMTP command specific restrictions described under
smtpd\_recipient\_restrictions. When recipient restrictions are listed
under smtpd\_sender\_restrictions, they have effect only with
"smtpd\_delay\_reject = yes", so that $smtpd\_sender\_restrictions is
evaluated at the time of the RCPT TO command.



Examples:




```

smtpd\_sender\_restrictions = reject\_unknown\_sender\_domain
smtpd\_sender\_restrictions = reject\_unknown\_sender\_domain,
    check\_sender\_access hash:/etc/postfix/access

```

