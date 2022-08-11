# local_header_rewrite_clients (default: permit_inet_interfaces)
 Rewrite message header addresses in mail from these clients and
update incomplete addresses with the domain name in $myorigin or
$mydomain; either don't rewrite message headers from other clients
at all, or rewrite message headers and update incomplete addresses
with the domain specified in the remote\_header\_rewrite\_domain
parameter. 


 See the append\_at\_myorigin and append\_dot\_mydomain parameters
for details of how domain names are appended to incomplete addresses.



 Specify a list of zero or more of the following: 



**permit\_inet\_interfaces**
 Append the domain name in $myorigin or $mydomain when the
client IP address matches $inet\_interfaces. This is enabled by
default. 
**permit\_mynetworks**
 Append the domain name in $myorigin or $mydomain when the
client IP address matches any network or network address listed in
$mynetworks. This setting will not prevent remote mail header
address rewriting when mail from a remote client is forwarded by
a neighboring system. 
**permit\_sasl\_authenticated** 
 Append the domain name in $myorigin or $mydomain when the
client is successfully authenticated via the RFC 4954 (AUTH)
protocol. 
**permit\_tls\_clientcerts** 
 Append the domain name in $myorigin or $mydomain when the
remote SMTP client TLS certificate fingerprint or public key fingerprint
(Postfix 2.9 and later) is listed in $relay\_clientcerts.
The fingerprint digest algorithm is configurable via the
smtpd\_tls\_fingerprint\_digest parameter (hard-coded as md5 prior to
Postfix version 2.5). 
 The default algorithm is **sha256** with Postfix ≥ 3.6
and the **compatibility\_level** set to 3.6 or higher. With Postfix
≤ 3.5, the default algorithm is **md5**. The best-practice
algorithm is now **sha256**. Recent advances in hash function
cryptanalysis have led to md5 and sha1 being deprecated in favor of
sha256. However, as long as there are no known "second pre-image"
attacks against the older algorithms, their use in this context, though
not recommended, is still likely safe. 
**permit\_tls\_all\_clientcerts** 
 Append the domain name in $myorigin or $mydomain when the
remote SMTP client TLS certificate is successfully verified, regardless of
whether it is listed on the server, and regardless of the certifying
authority. 
**check\_address\_map *type:table*** 
***type:table*** 
 Append the domain name in $myorigin or $mydomain when the
client IP address matches the specified lookup table.
The lookup result is ignored, and no subnet lookup is done. This
is suitable for, e.g., pop-before-smtp lookup tables. 

 Examples: 


 The Postfix < 2.2 backwards compatible setting: always rewrite
message headers, and always append my own domain to incomplete
header addresses. 



> 
> 
> ```
> 
> local\_header\_rewrite\_clients = static:all
> 
> ```
> 
> 


 The purist (and default) setting: rewrite headers only in mail
from Postfix sendmail and in SMTP mail from this machine. 



> 
> 
> ```
> 
> local\_header\_rewrite\_clients = permit\_inet\_interfaces
> 
> ```
> 
> 


 The intermediate setting: rewrite header addresses and append
$myorigin or $mydomain information only with mail from Postfix
sendmail, from local clients, or from authorized SMTP clients. 


 Note: this setting will not prevent remote mail header address
rewriting when mail from a remote client is forwarded by a neighboring
system. 



> 
> 
> ```
> 
> local\_header\_rewrite\_clients = permit\_mynetworks,
>     permit\_sasl\_authenticated permit\_tls\_clientcerts
>     check\_address\_map hash:/etc/postfix/pop-before-smtp
> 
> ```
> 
> 


