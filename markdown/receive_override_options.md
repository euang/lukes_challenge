# receive_override_options (default: empty)
 Enable or disable recipient validation, built-in content
filtering, or address mapping. Typically, these are specified in
master.cf as command-line arguments for the smtpd(8), qmqpd(8) or
pickup(8) daemons. 


 Specify zero or more of the following options. The options
override main.cf settings and are either implemented by smtpd(8),
qmqpd(8), or pickup(8) themselves, or they are forwarded to the
cleanup server. 



**no\_unknown\_recipient\_checks**
Do not try to reject unknown recipients (SMTP server only).
This is typically specified AFTER an external content filter.

**no\_address\_mappings**
Disable canonical address mapping, virtual alias map expansion,
address masquerading, and automatic BCC (blind carbon-copy)
recipients. This is typically specified BEFORE an external content
filter. 
**no\_header\_body\_checks**
Disable header/body\_checks. This is typically specified AFTER
an external content filter. 
**no\_milters**
Disable Milter (mail filter) applications. This is typically
specified AFTER an external content filter. 


Note: when the "BEFORE content filter" receive\_override\_options
setting is specified in the main.cf file, specify the "AFTER content
filter" receive\_override\_options setting in master.cf (and vice
versa).




Examples:




```

receive\_override\_options =
    no\_unknown\_recipient\_checks, no\_header\_body\_checks
receive\_override\_options = no\_address\_mappings

```


This feature is available in Postfix 2.1 and later.



