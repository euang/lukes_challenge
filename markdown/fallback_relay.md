# fallback_relay (default: empty)

Optional list of relay hosts for SMTP destinations that can't be
found or that are unreachable. With Postfix 2.3 this parameter
is renamed to smtp\_fallback\_relay. 



By default, mail is returned to the sender when a destination is
not found, and delivery is deferred when a destination is unreachable.



 The fallback relays must be SMTP destinations. Specify a domain,
host, host:port, [host]:port, [address] or [address]:port; the form
[host] turns off MX lookups. If you specify multiple SMTP
destinations, Postfix will try them in the specified order. 


 Note: before Postfix 2.2, do not use the fallback\_relay feature
when relaying mail
for a backup or primary MX domain. Mail would loop between the
Postfix MX host and the fallback\_relay host when the final destination
is unavailable. 


* In main.cf specify "relay\_transport = relay",
* In master.cf specify "-o fallback\_relay =" (i.e., empty) at
the end of the relay entry.
* In transport maps, specify "relay:*nexthop...*"
as the right-hand side for backup or primary MX domain entries.


 Postfix version 2.2 and later will not use the fallback\_relay feature
for destinations that it is MX host for.



