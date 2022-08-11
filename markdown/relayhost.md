# relayhost (default: empty)

The next-hop destination(s) for non-local mail; overrides non-local
domains in recipient addresses. This information is overruled with
relay\_transport, sender\_dependent\_default\_transport\_maps,
default\_transport, sender\_dependent\_relayhost\_maps
and with the transport(5) table.




On an intranet, specify the organizational domain name. If your
internal DNS uses no MX records, specify the name of the intranet
gateway host instead.




In the case of SMTP or LMTP delivery, specify one or more destinations
in the form of a domain name, hostname, hostname:port, [hostname]:port,
[hostaddress] or [hostaddress]:port, separated by comma or whitespace.
The form [hostname] turns off MX lookups. Multiple destinations are
supported in Postfix 3.5 and later.




If you're connected via UUCP, see the UUCP\_README file for useful
information.




Examples:




```

relayhost = $mydomain
relayhost = [gateway.example.com]
relayhost = mail1.example:587, mail2.example:587
relayhost = [an.ip.add.ress]

```

