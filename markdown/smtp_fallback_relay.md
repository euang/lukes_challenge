# smtp_fallback_relay (default: $fallback_relay)
 Optional list of relay destinations that will be used when an
SMTP destination is not found, or when delivery fails due to a
non-permanent error. With Postfix 2.2 and earlier this parameter
is called fallback\_relay. 


 By default, smtp\_fallback\_relay is empty, mail is returned to
the sender when a destination is not found, and delivery is deferred
after it fails due to a non-permanent error. 


 With bulk email deliveries, it can be beneficial to run the
fallback relay MTA on the same host, so that it can reuse the sender
IP address. This speeds up deliveries that are delayed by IP-based
reputation systems (greylist, etc.). 


 The fallback relays must be SMTP destinations. Specify a domain,
host, host:port, [host]:port, [address] or [address]:port; the form
[host] turns off MX lookups. If you specify multiple SMTP
destinations, Postfix will try them in the specified order. 


 To prevent mailer loops between MX hosts and fall-back hosts,
Postfix version 2.2 and later will not use the fallback relays for
destinations that it is MX host for (assuming DNS lookup is turned on).



