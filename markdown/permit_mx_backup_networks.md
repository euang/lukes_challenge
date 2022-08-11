# permit_mx_backup_networks (default: empty)

Restrict the use of the permit\_mx\_backup SMTP access feature to
only domains whose primary MX hosts match the listed networks.
The parameter value syntax is the same as with the mynetworks
parameter; note, however, that the default value is empty. 


 Pattern matching of domain names is controlled by the presence
or absence of "permit\_mx\_backup\_networks" in the
parent\_domain\_matches\_subdomains parameter value. 


