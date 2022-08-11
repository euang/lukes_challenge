# smtp_helo_name (default: $myhostname)

The hostname to send in the SMTP HELO or EHLO command.




The default value is the machine hostname. Specify a hostname or
[ip.add.re.ss].




This information can be specified in the main.cf file for all SMTP
clients, or it can be specified in the master.cf file for a specific
client, for example:




> 
> 
> ```
> 
> /etc/postfix/master.cf:
>     mysmtp ... smtp -o smtp\_helo\_name=foo.bar.com
> 
> ```
> 
> 



This feature is available in Postfix 2.0 and later.



