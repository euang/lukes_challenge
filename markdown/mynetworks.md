# mynetworks (default: see "postconf -d" output)

The list of "trusted" remote SMTP clients that have more privileges than
"strangers".




In particular, "trusted" SMTP clients are allowed to relay mail
through Postfix. See the smtpd\_relay\_restrictions parameter
description in the postconf(5) manual.




You can specify the list of "trusted" network addresses by hand
or you can let Postfix do it for you (which is the default).
See the description of the mynetworks\_style parameter for more
information.




If you specify the mynetworks list by hand,
Postfix ignores the mynetworks\_style setting.



 Specify a list of network addresses or network/netmask patterns,
separated by commas and/or whitespace. Continue long lines by
starting the next line with whitespace. 


 The netmask specifies the number of bits in the network part
of a host address. You can also specify "/file/name" or "type:table"
patterns. A "/file/name" pattern is replaced by its contents; a
"type:table" lookup table is matched when a table entry matches a
lookup string (the lookup result is ignored). 


 The list is matched left to right, and the search stops on the
first match. Specify "!pattern" to exclude an address or network
block from the list. The form "!/file/name" is supported only
in Postfix version 2.4 and later. 


 Note 1: Pattern matching of domain names is controlled by the
presence or absence of "mynetworks" in the parent\_domain\_matches\_subdomains
parameter value. 


 Note 2: IP version 6 address information must be specified inside
[] in the mynetworks value, and in files specified with
"/file/name". IP version 6 addresses contain the ":" character,
and would otherwise be confused with a "type:table" pattern. 


 Note 3: CIDR ranges cannot be specified in hash tables. Use cidr
tables if CIDR ranges are used. 


 Examples: 



```

mynetworks = 127.0.0.0/8 168.100.189.0/28
mynetworks = !192.168.0.1, 192.168.0.0/28
mynetworks = 127.0.0.0/8 168.100.189.0/28 [::1]/128 [2001:240:587::]/64
mynetworks = $config\_directory/mynetworks
mynetworks = hash:/etc/postfix/network\_table
mynetworks = cidr:/etc/postfix/network\_table.cidr

```

