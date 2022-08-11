# smtp_address_verify_target (default: rcpt)
 In the context of email address verification, the SMTP protocol
stage that determines whether an email address is deliverable.
Specify one of "rcpt" or "data". The latter is needed with remote
SMTP servers that reject recipients after the DATA command. Use
transport\_maps to apply this feature selectively: 



> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     transport\_maps = hash:/etc/postfix/transport
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/transport:
>     smtp-domain-that-verifies-after-data    smtp-data-target:
>     lmtp-domain-that-verifies-after-data    lmtp-data-target:
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/master.cf:
>     smtp-data-target    unix    -    -    n    -    -    smtp
>         -o smtp\_address\_verify\_target=data
>     lmtp-data-target    unix    -    -    n    -    -    lmtp
>         -o lmtp\_address\_verify\_target=data
> 
> ```
> 
> 


 Unselective use of the "data" target does no harm, but will
result in unnecessary "lost connection after DATA" events at remote
SMTP/LMTP servers. 


 This feature is available in Postfix 3.0 and later. 


