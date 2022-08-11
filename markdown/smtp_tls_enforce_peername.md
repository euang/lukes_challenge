# smtp_tls_enforce_peername (default: yes)
 With mandatory TLS encryption, require that the remote SMTP
server hostname matches the information in the remote SMTP server
certificate. As of RFC 2487 the requirements for hostname checking
for MTA clients are not specified. 


 This option can be set to "no" to disable strict peer name
checking. This setting has no effect on sessions that are controlled
via the smtp\_tls\_per\_site table. 


 Disabling the hostname verification can make sense in a closed
environment where special CAs are created. If not used carefully,
this option opens the danger of a "man-in-the-middle" attack (the
CommonName of this attacker will be logged). 


 This feature is available in Postfix 2.2 and later. With
Postfix 2.3 and later use smtp\_tls\_security\_level instead. 


