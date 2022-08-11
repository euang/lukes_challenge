# smtpd_sasl_auth_enable (default: no)

Enable SASL authentication in the Postfix SMTP server. By default,
the Postfix SMTP server does not use authentication.




If a remote SMTP client is authenticated, the permit\_sasl\_authenticated
access restriction can be used to permit relay access, like this:




> 
> 
> ```
> 
> # With Postfix 2.10 and later, the mail relay policy is
> # preferably specified under smtpd\_relay\_restrictions.
> smtpd\_relay\_restrictions =
>     permit\_mynetworks, permit\_sasl\_authenticated, ...
> 
> ```
> 
> 
> ```
> 
> # With Postfix before 2.10, the relay policy can be
> # specified only under smtpd\_recipient\_restrictions.
> smtpd\_recipient\_restrictions =
>     permit\_mynetworks, permit\_sasl\_authenticated, ...
> 
> ```
> 
> 


 To reject all SMTP connections from unauthenticated clients,
specify "smtpd\_delay\_reject = yes" (which is the default) and use:




> 
> 
> ```
> 
> smtpd\_client\_restrictions = permit\_sasl\_authenticated, reject
> 
> ```
> 
> 



See the SASL\_README file for SASL configuration and operation details.



