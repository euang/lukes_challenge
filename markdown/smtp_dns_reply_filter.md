# smtp_dns_reply_filter (default: empty)
 Optional filter for Postfix SMTP client DNS lookup results.
Specify zero or more lookup tables. The lookup tables are searched
in the given order for a match with the DNS lookup result, converted
to the following form: 



```

    *name ttl class type preference value*

```

 The *class* field is always "IN", the *preference*
field exists only for MX records, the names of hosts, domains, etc.
end in ".", and those names are in ASCII form (xn--mumble form in
the case of UTF8 names). 


 When a match is found, the table lookup result specifies an
action. By default, the table query and the action name are
case-insensitive. Currently, only the **IGNORE** action is
implemented. 


 Notes: 


* Postfix DNS reply filters have no effect on implicit DNS
lookups through nsswitch.conf or equivalent mechanisms.
* The Postfix SMTP/LMTP client uses smtp\_dns\_reply\_filter
and lmtp\_dns\_reply\_filter only to discover a remote SMTP or LMTP
service (record types MX, A, AAAA, and TLSA). These lookups are
also made to implement the features reject\_unverified\_sender and
reject\_unverified\_recipient.
* The Postfix SMTP/LMTP client defers mail delivery when
a filter removes all lookup results from a successful query.
* Postfix SMTP server uses smtpd\_dns\_reply\_filter only to
look up MX, A, AAAA, and TXT records to implement the features
reject\_unknown\_helo\_hostname, reject\_unknown\_sender\_domain,
reject\_unknown\_recipient\_domain, reject\_rbl\_\*, and reject\_rhsbl\_\*.
* The Postfix SMTP server logs a warning or defers mail
delivery when a filter removes all lookup results from a successful
query.


 Example: ignore Google AAAA records in Postfix SMTP client DNS
lookups, because Google sometimes hard-rejects mail from IPv6 clients
with valid PTR etc. records. 



```

/etc/postfix/main.cf:
    smtp\_dns\_reply\_filter = pcre:/etc/postfix/smtp\_dns\_reply\_filter

```


```

/etc/postfix/smtp\_dns\_reply\_filter:
    # /domain ttl IN AAAA address/ action, all case-insensitive.
    # Note: the domain name ends in ".".
    /^\S+\.google\.com\.\s+\S+\s+\S+\s+AAAA\s+/ IGNORE

```

 This feature is available in Postfix 3.0 and later. 


