# smtp_quote_rfc821_envelope (default: yes)

Quote addresses in Postfix SMTP client MAIL FROM and RCPT TO commands
as required
by RFC 5321. This includes putting quotes around an address localpart
that ends in ".".




The default is to comply with RFC 5321. If you have to send mail to
a broken SMTP server, configure a special SMTP client in master.cf:




> 
> 
> ```
> 
> /etc/postfix/master.cf:
>     broken-smtp . . . smtp -o smtp\_quote\_rfc821\_envelope=no
> 
> ```
> 
> 



and route mail for the destination in question to the "broken-smtp"
message delivery with a transport(5) table.




This feature is available in Postfix 2.1 and later.



