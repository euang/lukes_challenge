# proxy_interfaces (default: empty)

The remote network interface addresses that this mail system receives mail
on by way of a proxy or network address translation unit.




This feature is available in Postfix 2.0 and later.



 You must specify your "outside" proxy/NAT addresses when your
system is a backup MX host for other domains, otherwise mail delivery
loops will happen when the primary MX host is down. 



Example:




```

proxy\_interfaces = 1.2.3.4

```

