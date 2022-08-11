# content_filter (default: empty)
 After the message is queued, send the entire message to the
specified *transport:destination*. The *transport* name
specifies the first field of a mail delivery agent definition in
master.cf; the syntax of the next-hop *destination* is described
in the manual page of the corresponding delivery agent. More
information about external content filters is in the Postfix
FILTER\_README file. 


 Notes: 


* This setting has lower precedence than a FILTER action
that is specified in an access(5), header\_checks(5) or body\_checks(5)
table.
* The meaning of an empty next-hop filter *destination*
is version dependent. Postfix 2.7 and later will use the recipient
domain; earlier versions will use $myhostname. Specify
"default\_filter\_nexthop = $myhostname" for compatibility with Postfix
2.6 or earlier, or specify a content\_filter value with an explicit
next-hop *destination*.


