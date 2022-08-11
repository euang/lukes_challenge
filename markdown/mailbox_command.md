# mailbox_command (default: empty)

Optional external command that the local(8) delivery agent should
use for mailbox delivery. The command is run with the user ID and
the primary group ID privileges of the recipient. Exception:
command delivery for root executes with $default\_privs privileges.
This is not a problem, because 1) mail for root should always be
aliased to a real user and 2) don't log in as root, use "su" instead.




The following environment variables are exported to the command:




**CLIENT\_ADDRESS**
Remote client network address. Available in Postfix version 2.2 and
later. 
**CLIENT\_HELO**
Remote client EHLO command parameter. Available in Postfix version 2.2
and later.
**CLIENT\_HOSTNAME**
Remote client hostname. Available in Postfix version 2.2 and later.

**CLIENT\_PROTOCOL**
Remote client protocol. Available in Postfix version 2.2 and later.

**DOMAIN**
The domain part of the recipient address. 
**EXTENSION**
The optional address extension. 
**HOME**
The recipient home directory. 
**LOCAL**
The recipient address localpart. 
**LOGNAME**
The recipient's username. 
**ORIGINAL\_RECIPIENT**
The entire recipient address, before any address rewriting or
aliasing. 
**RECIPIENT**
The full recipient address. 
**SASL\_METHOD**
SASL authentication method specified in the remote client AUTH
command. Available in Postfix version 2.2 and later. 
**SASL\_SENDER**
SASL sender address specified in the remote client MAIL FROM
command. Available in Postfix version 2.2 and later. 
**SASL\_USER**
SASL username specified in the remote client AUTH command.
Available in Postfix version 2.2 and later. 
**SENDER**
The full sender address. 
**SHELL**
The recipient's login shell. 
**USER**
The recipient username. 


Unlike other Postfix configuration parameters, the mailbox\_command
parameter is not subjected to $name substitutions. This is to make
it easier to specify shell syntax (see example below).




If you can, avoid shell meta characters because they will force
Postfix to run an expensive shell process. If you're delivering
via "procmail" then running a shell won't make a noticeable difference
in the total cost.




Note: if you use the mailbox\_command feature to deliver mail
system-wide, you must set up an alias that forwards mail for root
to a real user.



 The precedence of local(8) delivery features from high to low
is: aliases, .forward files, mailbox\_transport\_maps, mailbox\_transport,
mailbox\_command\_maps, mailbox\_command, home\_mailbox, mail\_spool\_directory,
fallback\_transport\_maps, fallback\_transport and luser\_relay. 



Examples:




```

mailbox\_command = /some/where/procmail
mailbox\_command = /some/where/procmail -a "$EXTENSION"
mailbox\_command = /some/where/maildrop -d "$USER"
        -f "$SENDER" "$EXTENSION"

```

