# parent_domain_matches_subdomains (default: see "postconf -d" output)

A list of Postfix features where the pattern "example.com" also
matches subdomains of example.com,
instead of requiring an explicit ".example.com" pattern. This is
planned backwards compatibility: eventually, all Postfix features
are expected to require explicit ".example.com" style patterns when
you really want to match subdomains.



 The following Postfix feature names are supported. 



 Postfix version 1.0 and later

debug\_peer\_list,
fast\_flush\_domains,
mynetworks,
permit\_mx\_backup\_networks,
relay\_domains,
transport\_maps

 Postfix version 1.1 and later

qmqpd\_authorized\_clients,
smtpd\_access\_maps,

 Postfix version 2.8 and later 

postscreen\_access\_list

 Postfix version 3.0 and later 

smtpd\_client\_event\_limit\_exceptions


