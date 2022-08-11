# default_rbl_reply (default: see "postconf -d" output)

The default Postfix SMTP server response template for a request that is
rejected by an RBL-based restriction. This template can be overruled
by specific entries in the optional rbl\_reply\_maps lookup table.




This feature is available in Postfix 2.0 and later.




The template does not support Postfix configuration parameter $name
substitution. Instead, it supports exactly one level of $name
substitution for the following attributes:




**$client**
The client hostname and IP address, formatted as name[address]. 
**$client\_address**
The client IP address. 
**$client\_name**
The client hostname or "unknown". See reject\_unknown\_client\_hostname
for more details. 
**$reverse\_client\_name**
The client hostname from address->name lookup, or "unknown".
See reject\_unknown\_reverse\_client\_hostname for more details. 
**$helo\_name**
The hostname given in HELO or EHLO command or empty string. 
**$rbl\_class**
The denylisted entity type: Client host, Helo command, Sender
address, or Recipient address. 
**$rbl\_code**
The numerical SMTP response code, as specified with the
maps\_rbl\_reject\_code configuration parameter. Note: The numerical
SMTP response code is required, and must appear at the start of the
reply. With Postfix version 2.3 and later this information may be followed
by an RFC 3463 enhanced status code. 
**$rbl\_domain**
The RBL domain where $rbl\_what is denylisted. 
**$rbl\_reason**
The reason why $rbl\_what is denylisted, or an empty string. 
**$rbl\_what**
The entity that is denylisted (an IP address, a hostname, a domain
name, or an email address whose domain was denylisted). 
**$recipient**
The recipient address or <> in case of the null address. 
**$recipient\_domain**
The recipient domain or empty string. 
**$recipient\_name**
The recipient address localpart or <> in case of null address. 
**$sender**
The sender address or <> in case of the null address. 
**$sender\_domain**
The sender domain or empty string. 
**$sender\_name**
The sender address localpart or <> in case of the null address. 
**${name?value}**
**${name?{value}}** (Postfix ≥ 3.0)
Expands to *value* when *$name* is non-empty. 
**${name:value}**
**${name:{value}}** (Postfix ≥ 3.0)
Expands to *value* when *$name* is empty. 
**${name?{value1}:{value2}}** (Postfix ≥ 3.0)
Expands to *value1* when *$name* is non-empty,
*value2* otherwise. 


Instead of $name you can also specify ${name} or $(name).



 Note: when an enhanced status code is specified in an RBL reply
template, it is subject to modification. The following transformations
are needed when the same RBL reply template is used for client,
helo, sender, or recipient access restrictions. 


* When rejecting a sender address, the Postfix SMTP server
will transform a recipient DSN status (e.g., 4.1.1-4.1.6) into the
corresponding sender DSN status, and vice versa.
* When rejecting non-address information (such as the HELO
command argument or the client hostname/address), the Postfix SMTP
server will transform a sender or recipient DSN status into a generic
non-address DSN status (e.g., 4.0.0).


