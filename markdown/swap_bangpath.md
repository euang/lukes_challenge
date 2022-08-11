# swap_bangpath (default: yes)

Enable the rewriting of "site!user" into "user@site". This is
necessary if your machine is connected to UUCP networks. It is
enabled by default.



 Note: with Postfix version 2.2, message header address rewriting
happens only when one of the following conditions is true: 


* The message is received with the Postfix sendmail(1) command,
* The message is received from a network client that matches
$local\_header\_rewrite\_clients,
* The message is received from the network, and the
remote\_header\_rewrite\_domain parameter specifies a non-empty value.


 To get the behavior before Postfix version 2.2, specify
"local\_header\_rewrite\_clients = static:all". 



Example:




```

swap\_bangpath = no

```

