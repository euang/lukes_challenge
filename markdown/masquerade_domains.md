# masquerade_domains (default: empty)

Optional list of domains whose subdomain structure will be stripped
off in email addresses.




The list is processed left to right, and processing stops at the
first match. Thus,




> 
> 
> ```
> 
> masquerade\_domains = foo.example.com example.com
> 
> ```
> 
> 



strips "user@any.thing.foo.example.com" to "user@foo.example.com",
but strips "user@any.thing.else.example.com" to "user@example.com".




A domain name prefixed with ! means do not masquerade this domain
or its subdomains. Thus,




> 
> 
> ```
> 
> masquerade\_domains = !foo.example.com example.com
> 
> ```
> 
> 



does not change "user@any.thing.foo.example.com" or "user@foo.example.com",
but strips "user@any.thing.else.example.com" to "user@example.com".



 Note: with Postfix version 2.2, message header address masquerading
happens only when message header address rewriting is enabled: 


* The message is received with the Postfix sendmail(1) command,
* The message is received from a network client that matches
$local\_header\_rewrite\_clients,
* The message is received from the network, and the
remote\_header\_rewrite\_domain parameter specifies a non-empty value.


 To get the behavior before Postfix version 2.2, specify
"local\_header\_rewrite\_clients = static:all". 



Example:




```

masquerade\_domains = $mydomain

```

