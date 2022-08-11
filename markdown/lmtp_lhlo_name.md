# lmtp_lhlo_name (default: $myhostname)

The hostname to send in the LMTP LHLO command.




The default value is the machine hostname. Specify a hostname or
[ip.add.re.ss] or [ip:v6:add:re::ss].




This information can be specified in the main.cf file for all LMTP
clients, or it can be specified in the master.cf file for a specific
client, for example:




> 
> 
> ```
> 
> /etc/postfix/master.cf:
>     mylmtp ... lmtp -o lmtp\_lhlo\_name=foo.bar.com
> 
> ```
> 
> 



This feature is available in Postfix 2.3 and later.



