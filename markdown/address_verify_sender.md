# address_verify_sender (default: $double_bounce_sender)
 The sender address to use in address verification probes; prior
to Postfix 2.5 the default was "postmaster". To
avoid problems with address probes that are sent in response to
address probes, the Postfix SMTP server excludes the probe sender
address from all SMTPD access blocks. 



Specify an empty value (address\_verify\_sender =) or <> if you want
to use the null sender address. Beware, some sites reject mail from
<>, even though RFCs require that such addresses be accepted.




Examples:




```

address\_verify\_sender = <>
address\_verify\_sender = postmaster@my.domain

```


This feature is available in Postfix 2.1 and later.



