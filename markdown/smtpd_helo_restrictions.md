# smtpd_helo_restrictions (default: empty)

Optional restrictions that the Postfix SMTP server applies in the
context of a client HELO command.
See SMTPD\_ACCESS\_README, section "Delayed evaluation of SMTP access
restriction lists" for a discussion of evaluation context and time.




The default is to permit everything.



 Note: specify "smtpd\_helo\_required = yes" to fully enforce this
restriction (without "smtpd\_helo\_required = yes", a client can
simply skip smtpd\_helo\_restrictions by not sending HELO or EHLO).




Specify a list of restrictions, separated by commas and/or whitespace.
Continue long lines by starting the next line with whitespace.
Restrictions are applied in the order as specified; the first
restriction that matches wins.




The following restrictions are specific to the hostname information
received with the HELO or EHLO command.




**check\_helo\_access *type:table***
Search the specified access(5) database for the HELO or EHLO
hostname or parent domains, and execute the corresponding action.
Note: specify "smtpd\_helo\_required = yes" to fully enforce this
restriction (without "smtpd\_helo\_required = yes", a client can
simply skip check\_helo\_access by not sending HELO or EHLO). 
**check\_helo\_a\_access *type:table***
Search the specified access(5) database for the IP addresses for
the HELO or EHLO hostname, and execute the corresponding action.
Note 1: a result of "OK" is not allowed for safety reasons. Instead,
use DUNNO in order to exclude specific hosts from denylists. Note
2: specify "smtpd\_helo\_required = yes" to fully enforce this
restriction (without "smtpd\_helo\_required = yes", a client can
simply skip check\_helo\_a\_access by not sending HELO or EHLO). This
feature is available in Postfix 3.0 and later.

**check\_helo\_mx\_access *type:table***
Search the specified access(5) database for the MX hosts for
the HELO or EHLO hostname, and execute the corresponding action.
If no MX record is found, look up A or AAAA records, just like the
Postfix SMTP client would.
Note 1: a result of "OK" is not allowed for safety reasons. Instead,
use DUNNO in order to exclude specific hosts from denylists. Note
2: specify "smtpd\_helo\_required = yes" to fully enforce this
restriction (without "smtpd\_helo\_required = yes", a client can
simply skip check\_helo\_mx\_access by not sending HELO or EHLO). This
feature is available in Postfix 2.1 and later.

**check\_helo\_ns\_access *type:table***
Search the specified access(5) database for the DNS servers
for the HELO or EHLO hostname, and execute the corresponding action.
Note 1: a result of "OK" is not allowed for safety reasons. Instead,
use DUNNO in order to exclude specific hosts from denylists. Note
2: specify "smtpd\_helo\_required = yes" to fully enforce this
restriction (without "smtpd\_helo\_required = yes", a client can
simply skip check\_helo\_ns\_access by not sending HELO or EHLO). This
feature is available in Postfix 2.1 and later.

**reject\_invalid\_helo\_hostname** (with Postfix < 2.3: reject\_invalid\_hostname)
Reject the request when the HELO or EHLO hostname is malformed.
Note: specify "smtpd\_helo\_required = yes" to fully enforce
this restriction (without "smtpd\_helo\_required = yes", a client can simply
skip reject\_invalid\_helo\_hostname by not sending HELO or EHLO).
  
 The invalid\_hostname\_reject\_code specifies the response code
for rejected requests (default: 501).
**reject\_non\_fqdn\_helo\_hostname** (with Postfix < 2.3: reject\_non\_fqdn\_hostname)
Reject the request when the HELO or EHLO hostname is not in
fully-qualified domain or address literal form, as required by the
RFC. Note: specify
"smtpd\_helo\_required = yes" to fully enforce this restriction
(without "smtpd\_helo\_required = yes", a client can simply skip
reject\_non\_fqdn\_helo\_hostname by not sending HELO or EHLO).   

The non\_fqdn\_reject\_code parameter specifies the response code for
rejected requests (default: 504).
**reject\_rhsbl\_helo *rbl\_domain=d.d.d.d***
Reject the request when the HELO or EHLO hostname is
listed with the A record "*d.d.d.d*" under *rbl\_domain*
(Postfix version 2.1 and later only). Each "*d*" is a number,
or a pattern inside "[]" that contains one or more ";"-separated
numbers or number..number ranges (Postfix version 2.8 and later).
If no "*=d.d.d.d*" is
specified, reject the request when the HELO or EHLO hostname is
listed with any A record under *rbl\_domain*. See the
reject\_rbl\_client description for additional RBL related configuration
parameters. Note: specify "smtpd\_helo\_required = yes" to fully
enforce this restriction (without "smtpd\_helo\_required = yes", a
client can simply skip reject\_rhsbl\_helo by not sending HELO or
EHLO). This feature is available in Postfix 2.0
and later. 
**reject\_unknown\_helo\_hostname** (with Postfix < 2.3: reject\_unknown\_hostname)
Reject the request when the HELO or EHLO hostname has no DNS A
or MX record.   
 The reply is specified with the
unknown\_hostname\_reject\_code parameter (default: 450) or
unknown\_helo\_hostname\_tempfail\_action (default: defer\_if\_permit).
See the respective parameter descriptions for details.   

Note: specify "smtpd\_helo\_required = yes" to fully
enforce this restriction (without "smtpd\_helo\_required = yes", a
client can simply skip reject\_unknown\_helo\_hostname by not sending
HELO or EHLO). 


Other restrictions that are valid in this context:



* Generic restrictions that can be used
in any SMTP command context, described under smtpd\_client\_restrictions.
* Client hostname or network address specific restrictions
described under smtpd\_client\_restrictions.
* SMTP command specific restrictions described under
smtpd\_sender\_restrictions or smtpd\_recipient\_restrictions. When
sender or recipient restrictions are listed under smtpd\_helo\_restrictions,
they have effect only with "smtpd\_delay\_reject = yes", so that
$smtpd\_helo\_restrictions is evaluated at the time of the RCPT TO
command.



Examples:




```

smtpd\_helo\_restrictions = permit\_mynetworks, reject\_invalid\_helo\_hostname
smtpd\_helo\_restrictions = permit\_mynetworks, reject\_unknown\_helo\_hostname

```

