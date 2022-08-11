# smtpd_sasl_security_options (default: noanonymous)
 Postfix SMTP server SASL security options; as of Postfix 2.3
the list of available
features depends on the SASL server implementation that is selected
with **smtpd\_sasl\_type**. 


 The following security features are defined for the **cyrus**
server SASL implementation: 



Restrict what authentication mechanisms the Postfix SMTP server
will offer to the client. The list of available authentication
mechanisms is system dependent.




Specify zero or more of the following:




**noplaintext**
Disallow methods that use plaintext passwords. 
**noactive**
Disallow methods subject to active (non-dictionary) attack. 
**nodictionary**
Disallow methods subject to passive (dictionary) attack. 
**noanonymous**
Disallow methods that allow anonymous authentication. 
**forward\_secrecy**
Only allow methods that support forward secrecy (Dovecot only).

**mutual\_auth**
Only allow methods that provide mutual authentication (not available
with Cyrus SASL version 1). 


By default, the Postfix SMTP server accepts plaintext passwords but
not anonymous logins.




Warning: it appears that clients try authentication methods in the
order as advertised by the server (e.g., PLAIN ANONYMOUS CRAM-MD5)
which means that if you disable plaintext passwords, clients will
log in anonymously, even when they should be able to use CRAM-MD5.
So, if you disable plaintext logins, disable anonymous logins too.
Postfix treats anonymous login as no authentication.




Example:




```

smtpd\_sasl\_security\_options = noanonymous, noplaintext

```

