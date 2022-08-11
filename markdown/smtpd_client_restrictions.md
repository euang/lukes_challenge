# smtpd_client_restrictions (default: empty)

Optional restrictions that the Postfix SMTP server applies in the
context of a client connection request.
See SMTPD\_ACCESS\_README, section "Delayed evaluation of SMTP access
restriction lists" for a discussion of evaluation context and time.




The default is to allow all connection requests.




Specify a list of restrictions, separated by commas and/or whitespace.
Continue long lines by starting the next line with whitespace.
Restrictions are applied in the order as specified; the first
restriction that matches wins.




The following restrictions are specific to client hostname or
client network address information.




**check\_ccert\_access *type:table***
 By default use the remote SMTP client certificate fingerprint
or the public key
fingerprint (Postfix 2.9 and later) as the lookup key for the specified
access(5) database; with Postfix version 2.2, also require that the
remote SMTP client certificate is verified successfully.
The fingerprint digest algorithm is configurable via the
smtpd\_tls\_fingerprint\_digest parameter (hard-coded as md5 prior to
Postfix version 2.5). This feature requires "smtpd\_tls\_ask\_ccert
= yes" and is available with Postfix version
2.2 and later. 
 The default algorithm is **sha256** with Postfix ≥ 3.6
and the **compatibility\_level** set to 3.6 or higher. With Postfix
≤ 3.5, the default algorithm is **md5**. The best-practice
algorithm is now **sha256**. Recent advances in hash function
cryptanalysis have led to md5 and sha1 being deprecated in favor of
sha256. However, as long as there are no known "second pre-image"
attacks against the older algorithms, their use in this context, though
not recommended, is still likely safe. 
 Alternatively, check\_ccert\_access accepts an explicit search
order (Postfix 3.5 and later). The default search order as described
above corresponds with: 
 check\_ccert\_access { type:table, { search\_order = cert\_fingerprint,
pubkey\_fingerprint } } 
 The commas are optional. 
**check\_client\_access *type:table***
Search the specified access database for the client hostname,
parent domains, client IP address, or networks obtained by stripping
least significant octets. See the access(5) manual page for details. 
**check\_client\_a\_access *type:table***
Search the specified access(5) database for the IP addresses for the
client hostname, and execute the corresponding action. Note: a result
of "OK" is not allowed for safety reasons. Instead, use DUNNO in order
to exclude specific hosts from denylists. This feature is available
in Postfix 3.0 and later. 
**check\_client\_mx\_access *type:table***
Search the specified access(5) database for the MX hosts for the
client hostname, and execute the corresponding action. If no MX
record is found, look up A or AAAA records, just like the Postfix
SMTP client would. Note: a result
of "OK" is not allowed for safety reasons. Instead, use DUNNO in order
to exclude specific hosts from denylists. This feature is available
in Postfix 2.7 and later. 
**check\_client\_ns\_access *type:table***
Search the specified access(5) database for the DNS servers for
the client hostname, and execute the corresponding action. Note: a
result of "OK" is not allowed for safety reasons. Instead, use DUNNO
in order to exclude specific hosts from denylists. This feature is
available in Postfix 2.7 and later. 
**check\_reverse\_client\_hostname\_access *type:table***
Search the specified access database for the unverified reverse
client hostname, parent domains, client IP address, or networks
obtained by stripping least significant octets. See the access(5)
manual page for details. Note: a result of "OK" is not allowed for
safety reasons. Instead, use DUNNO in order to exclude specific
hosts from denylists. This feature is available in Postfix 2.6
and later.
**check\_reverse\_client\_hostname\_a\_access *type:table***
Search the specified access(5) database for the IP addresses for the
unverified reverse client hostname, and execute the corresponding
action. Note: a result of "OK" is not allowed for safety reasons.
Instead, use DUNNO in order to exclude specific hosts from denylists.
This feature is available in Postfix 3.0 and later. 
**check\_reverse\_client\_hostname\_mx\_access *type:table***
Search the specified access(5) database for the MX hosts for the
unverified reverse client hostname, and execute the corresponding
action. If no MX record is found, look up A or AAAA records, just
like the Postfix SMTP client would.
Note: a result of "OK" is not allowed for safety reasons.
Instead, use DUNNO in order to exclude specific hosts from denylists.
This feature is available in Postfix 2.7 and later. 
**check\_reverse\_client\_hostname\_ns\_access *type:table***
Search the specified access(5) database for the DNS servers for
the unverified reverse client hostname, and execute the corresponding
action. Note: a result of "OK" is not allowed for safety reasons.
Instead, use DUNNO in order to exclude specific hosts from denylists.
This feature is available in Postfix 2.7 and later. 
**check\_sasl\_access *type:table***
 Use the remote SMTP client SASL user name as the lookup key for
the specified access(5) database. The lookup key has the form
"username@domainname" when the smtpd\_sasl\_local\_domain parameter
value is non-empty. Unlike the check\_client\_access feature,
check\_sasl\_access does not perform matches of parent domains or IP
subnet ranges. This feature is available with Postfix version 2.11
and later. 
**permit\_inet\_interfaces**
Permit the request when the client IP address matches
$inet\_interfaces. 
**permit\_mynetworks**
Permit the request when the client IP address matches any
network or network address listed in $mynetworks. 
**permit\_sasl\_authenticated**
 Permit the request when the client is successfully
authenticated via the RFC 4954 (AUTH) protocol. 
**permit\_tls\_all\_clientcerts**
 Permit the request when the remote SMTP client certificate is
verified successfully. This option must be used only if a special
CA issues the certificates and only this CA is listed as a trusted
CA. Otherwise, clients with a third-party certificate would also
be allowed to relay. Specify "tls\_append\_default\_CA = no" when the
trusted CA is specified with smtpd\_tls\_CAfile or smtpd\_tls\_CApath,
to prevent Postfix from appending the system-supplied default CAs.
This feature requires "smtpd\_tls\_ask\_ccert = yes" and is available
with Postfix version 2.2 and later.
**permit\_tls\_clientcerts**
Permit the request when the remote SMTP client certificate
fingerprint or public key fingerprint (Postfix 2.9 and later) is
listed in $relay\_clientcerts.
The fingerprint digest algorithm is configurable via the
smtpd\_tls\_fingerprint\_digest parameter (hard-coded as md5 prior to
Postfix version 2.5). This feature requires "smtpd\_tls\_ask\_ccert
= yes" and is available with Postfix version 2.2 and later.
 The default algorithm is **sha256** with Postfix ≥ 3.6
and the **compatibility\_level** set to 3.6 or higher. With Postfix
≤ 3.5, the default algorithm is **md5**. The best-practice
algorithm is now **sha256**. Recent advances in hash function
cryptanalysis have led to md5 and sha1 being deprecated in favor of
sha256. However, as long as there are no known "second pre-image"
attacks against the older algorithms, their use in this context, though
not recommended, is still likely safe. 
**reject\_rbl\_client *rbl\_domain=d.d.d.d***
Reject the request when the reversed client network address is
listed with the A record "*d.d.d.d*" under *rbl\_domain*
(Postfix version 2.1 and later only). Each "*d*" is a number,
or a pattern inside "[]" that contains one or more ";"-separated
numbers or number..number ranges (Postfix version 2.8 and later).
If no "*=d.d.d.d*" is specified, reject the request when the
reversed client network address is listed with any A record under
*rbl\_domain*.   

The maps\_rbl\_reject\_code parameter specifies the response code for
rejected requests (default: 554), the default\_rbl\_reply parameter
specifies the default server reply, and the rbl\_reply\_maps parameter
specifies tables with server replies indexed by *rbl\_domain*.
This feature is available in Postfix 2.0 and later. 
**permit\_dnswl\_client *dnswl\_domain=d.d.d.d***
Accept the request when the reversed client network address is
listed with the A record "*d.d.d.d*" under *dnswl\_domain*.
Each "*d*" is a number, or a pattern inside "[]" that contains
one or more ";"-separated numbers or number..number ranges.
If no "*=d.d.d.d*" is specified, accept the request when the
reversed client network address is listed with any A record under
*dnswl\_domain*.   
 For safety, permit\_dnswl\_client is silently
ignored when it would override reject\_unauth\_destination. The
result is DEFER\_IF\_REJECT when allowlist lookup fails. This feature
is available in Postfix 2.8 and later. 
**reject\_rhsbl\_client *rbl\_domain=d.d.d.d***
Reject the request when the client hostname is listed with the
A record "*d.d.d.d*" under *rbl\_domain* (Postfix version
2.1 and later only). Each "*d*" is a number, or a pattern
inside "[]" that contains one or more ";"-separated numbers or
number..number ranges (Postfix version 2.8 and later). If no
"*=d.d.d.d*" is specified, reject the request when the client
hostname is listed with
any A record under *rbl\_domain*. See the reject\_rbl\_client
description above for additional RBL related configuration parameters.
This feature is available in Postfix 2.0 and later; with Postfix
version 2.8 and later, reject\_rhsbl\_reverse\_client will usually
produce better results. 
**permit\_rhswl\_client *rhswl\_domain=d.d.d.d***
Accept the request when the client hostname is listed with the
A record "*d.d.d.d*" under *rhswl\_domain*. Each "*d*"
is a number, or a pattern inside "[]" that contains one or more
";"-separated numbers or number..number ranges. If no
"*=d.d.d.d*" is specified, accept the request when the client
hostname is listed with any A record under *rhswl\_domain*.
  
 Caution: client name allowlisting is fragile, since the client
name lookup can fail due to temporary outages. Client name
allowlisting should be used only to reduce false positives in e.g.
DNS-based blocklists, and not for making access rule exceptions.
  
 For safety, permit\_rhswl\_client is silently ignored when it
would override reject\_unauth\_destination. The result is DEFER\_IF\_REJECT
when allowlist lookup fails. This feature is available in Postfix
2.8 and later. 
**reject\_rhsbl\_reverse\_client *rbl\_domain=d.d.d.d***
Reject the request when the unverified reverse client hostname
is listed with the A record "*d.d.d.d*" under *rbl\_domain*.
Each "*d*" is a number, or a pattern inside "[]" that contains
one or more ";"-separated numbers or number..number ranges.
If no "*=d.d.d.d*" is specified, reject the request when the
unverified reverse client hostname is listed with any A record under
*rbl\_domain*. See the reject\_rbl\_client description above for
additional RBL related configuration parameters. This feature is
available in Postfix 2.8 and later. 
**reject\_unknown\_client\_hostname** (with Postfix < 2.3: reject\_unknown\_client)
Reject the request when 1) the client IP address->name mapping
fails, or 2) the name->address mapping fails, or 3) the name->address
mapping does not match the client IP address.   
 This is a
stronger restriction than the reject\_unknown\_reverse\_client\_hostname
feature, which triggers only under condition 1) above.   
 The
unknown\_client\_reject\_code parameter specifies the response code
for rejected requests (default: 450). The reply is always 450 in
case the address->name or name->address lookup failed due to
a temporary problem. 
**reject\_unknown\_reverse\_client\_hostname**
Reject the request when the client IP address has no address->name
mapping.   
 This is a weaker restriction than the
reject\_unknown\_client\_hostname feature, which requires not only
that the address->name and name->address mappings exist, but
also that the two mappings reproduce the client IP address.   

The unknown\_client\_reject\_code parameter specifies the response
code for rejected requests (default: 450). The reply is always 450
in case the address->name lookup failed due to a temporary
problem.   
 This feature is available in Postfix 2.3 and
later. 


In addition, you can use any of the following 
generic restrictions. These restrictions are applicable in
any SMTP command context.




**check\_policy\_service *servername***
Query the specified policy server. See the SMTPD\_POLICY\_README
document for details. This feature is available in Postfix 2.1
and later. 
**defer**
Defer the request. The client is told to try again later. This
restriction is useful at the end of a restriction list, to make
the default policy explicit.   
 The defer\_code parameter specifies
the SMTP server reply code (default: 450).
**defer\_if\_permit**
Defer the request if some later restriction would result in an
explicit or implicit PERMIT action. This is useful when a denylisting
feature fails due to a temporary problem. This feature is available
in Postfix version 2.1 and later. 
**defer\_if\_reject**
Defer the request if some later restriction would result in a
REJECT action. This is useful when an allowlisting feature fails
due to a temporary problem. This feature is available in Postfix
version 2.1 and later. 
**permit**
Permit the request. This restriction is useful at the end of
a restriction list, to make the default policy explicit.
**reject\_multi\_recipient\_bounce**
Reject the request when the envelope sender is the null address,
and the message has multiple envelope recipients. This usage has
rare but legitimate applications: under certain conditions,
multi-recipient mail that was posted with the DSN option NOTIFY=NEVER
may be forwarded with the null sender address.
  
 Note: this restriction can only work reliably
when used in smtpd\_data\_restrictions or
smtpd\_end\_of\_data\_restrictions, because the total number of
recipients is not known at an earlier stage of the SMTP conversation.
Use at the RCPT stage will only reject the second etc. recipient.
  

The multi\_recipient\_bounce\_reject\_code parameter specifies the
response code for rejected requests (default: 550). This feature
is available in Postfix 2.1 and later. 
**reject\_plaintext\_session**
Reject the request when the connection is not encrypted. This
restriction should not be used before the client has had a chance
to negotiate encryption with the AUTH or STARTTLS commands.
  

The plaintext\_reject\_code parameter specifies the response
code for rejected requests (default: 450). This feature is available
in Postfix 2.3 and later. 
**reject\_unauth\_pipelining**
Reject the request when the client sends SMTP commands ahead
of time where it is not allowed, or when the client sends SMTP
commands ahead of time without knowing that Postfix actually supports
ESMTP command pipelining. This stops mail from bulk mail software
that improperly uses ESMTP command pipelining in order to speed up
deliveries.
  
 With Postfix 2.6 and later, the SMTP server sets a per-session
flag whenever it detects illegal pipelining, including pipelined
HELO or EHLO commands. The reject\_unauth\_pipelining feature simply
tests whether the flag was set at any point in time during the
session.
  
 With older Postfix versions, reject\_unauth\_pipelining checks
the current status of the input read queue, and its usage is not
recommended in contexts other than smtpd\_data\_restrictions. 
**reject**
Reject the request. This restriction is useful at the end of
a restriction list, to make the default policy explicit. The
reject\_code configuration parameter specifies the response code for
rejected requests (default: 554).
**sleep *seconds***
Pause for the specified number of seconds and proceed with
the next restriction in the list, if any. This may stop zombie
mail when used as:

```

/etc/postfix/main.cf:
    smtpd\_client\_restrictions =
        sleep 1, reject\_unauth\_pipelining
    smtpd\_delay\_reject = no

```

This feature is available in Postfix 2.3. 
**warn\_if\_reject**
 A safety net for testing. When "warn\_if\_reject" is placed
before a reject-type restriction, access table query, or
check\_policy\_service query, this logs a "reject\_warning" message
instead of rejecting a request (when a reject-type restriction fails
due to a temporary error, this logs a "reject\_warning" message for
any implicit "defer\_if\_permit" actions that would normally prevent
mail from being accepted by some later access restriction). This
feature has no effect on defer\_if\_reject restrictions. 


Other restrictions that are valid in this context:



* SMTP command specific restrictions that are described under
the smtpd\_helo\_restrictions, smtpd\_sender\_restrictions or
smtpd\_recipient\_restrictions parameters. When helo, sender or
recipient restrictions are listed under smtpd\_client\_restrictions,
they have effect only with "smtpd\_delay\_reject = yes", so that
$smtpd\_client\_restrictions is evaluated at the time of the RCPT TO
command.



Example:




```

smtpd\_client\_restrictions = permit\_mynetworks, reject\_unknown\_client\_hostname

```

