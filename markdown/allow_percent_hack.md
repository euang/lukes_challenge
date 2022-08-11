# allow_percent_hack (default: yes)

Enable the rewriting of the form "user%domain" to "user@domain".
This is enabled by default.



 Note: as of Postfix version 2.2, message header address rewriting
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

allow\_percent\_hack = no

```

