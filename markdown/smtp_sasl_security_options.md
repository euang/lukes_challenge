# smtp_sasl_security_options (default: noplaintext, noanonymous)
 Postfix SMTP client SASL security options; as of Postfix 2.3
the list of available
features depends on the SASL client implementation that is selected
with **smtp\_sasl\_type**. 


 The following security features are defined for the **cyrus**
client SASL implementation: 



Specify zero or more of the following:




**noplaintext**
Disallow methods that use plaintext passwords. 
**noactive**
Disallow methods subject to active (non-dictionary) attack.

**nodictionary**
Disallow methods subject to passive (dictionary) attack. 
**noanonymous**
Disallow methods that allow anonymous authentication. 
**mutual\_auth**
Only allow methods that provide mutual authentication (not
available with SASL version 1). 


Example:




```

smtp\_sasl\_security\_options = noplaintext

```

