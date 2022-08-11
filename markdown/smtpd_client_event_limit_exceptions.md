# smtpd_client_event_limit_exceptions (default: $mynetworks)

Clients that are excluded from smtpd\_client\_\*\_count/rate\_limit
restrictions. See the mynetworks parameter
description for the parameter value syntax.




By default, clients in trusted networks are excluded. Specify a
list of network blocks, hostnames or .domain names (the initial
dot causes the domain to match any name below it).



 Note: IP version 6 address information must be specified inside
[] in the smtpd\_client\_event\_limit\_exceptions value, and
in files specified with "/file/name". IP version 6 addresses
contain the ":" character, and would otherwise be confused with a
"type:table" pattern. 


 Pattern matching of domain names is controlled by the presence
or absence of "smtpd\_client\_event\_limit\_exceptions" in the
parent\_domain\_matches\_subdomains parameter value (Postfix 3.0 and
later). 



This feature is available in Postfix 2.2 and later.



