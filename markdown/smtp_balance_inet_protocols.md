# smtp_balance_inet_protocols (default: yes)
 When a remote destination resolves to a combination of IPv4 and
IPv6 addresses, ensure that the Postfix SMTP client can try both
address types before it runs into the smtp\_mx\_address\_limit. 


 This avoids an interoperability problem when a destination resolves
to primarily IPv6 addresses, the smtp\_address\_limit feature eliminates
most or all IPv4 addresses, and the destination is not reachable over
IPv6. 


 This feature is available in Postfix 3.3 and later. 


