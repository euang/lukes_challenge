# relay_domains (default: Postfix ≥ 3.0: empty, Postfix < 3.0: $mydestination)
 What destination domains (and subdomains thereof) this system
will relay mail to. For details about how
the relay\_domains value is used, see the description of the
permit\_auth\_destination and reject\_unauth\_destination SMTP recipient
restrictions. 


 Domains that match $relay\_domains are delivered with the
$relay\_transport mail delivery transport. The SMTP server validates
recipient addresses with $relay\_recipient\_maps and rejects non-existent
recipients. See also the relay domains address class in the
ADDRESS\_CLASS\_README file. 


 Note: Postfix will not automatically forward mail for domains
that list this system as their primary or backup MX host. See the
permit\_mx\_backup restriction in the postconf(5) manual page. 


 Specify a list of host or domain names, "/file/name" patterns
or "type:table" lookup tables, separated by commas and/or whitespace.
Continue long lines by starting the next line with whitespace. A
"/file/name" pattern is replaced by its contents; a "type:table"
lookup table is matched when a (parent) domain appears as lookup
key. Specify "!pattern" to exclude a domain from the list. The form
"!/file/name" is supported only in Postfix version 2.4 and later.



 Pattern matching of domain names is controlled by the presence
or absence of "relay\_domains" in the parent\_domain\_matches\_subdomains
parameter value. 


