# postscreen_dnsbl_sites (default: empty)
Optional list of DNS allow/denylist domains, filters and weight
factors. When the list is non-empty, the dnsblog(8) daemon will
query these domains with the IP addresses of remote SMTP clients,
and postscreen(8) will update an SMTP client's DNSBL score with
each non-error reply. 


 Caution: when postscreen rejects mail, it replies with the DNSBL
domain name. Use the postscreen\_dnsbl\_reply\_map feature to hide
"password" information in DNSBL domain names. 


 When a client's score is equal to or greater than the threshold
specified with postscreen\_dnsbl\_threshold, postscreen(8) can drop
the connection with the remote SMTP client. 


 Specify a list of domain=filter\*weight entries, separated by
comma or whitespace. 


* When no "=filter" is specified, postscreen(8) will use any
non-error DNSBL reply. Otherwise, postscreen(8) uses only DNSBL
replies that match the filter. The filter has the form d.d.d.d,
where each d is a number, or a pattern inside [] that contains one
or more ";"-separated numbers or number..number ranges.
* When no "\*weight" is specified, postscreen(8) increments
the remote SMTP client's DNSBL score by 1. Otherwise, the weight must be
an integral number, and postscreen(8) adds the specified weight to
the remote SMTP client's DNSBL score. Specify a negative number for
allowlisting.
* When one postscreen\_dnsbl\_sites entry produces multiple
DNSBL responses, postscreen(8) applies the weight at most once.


 Examples: 


 To use example.com as a high-confidence blocklist, and to
block mail with example.net and example.org only when both agree:




```

postscreen\_dnsbl\_threshold = 2
postscreen\_dnsbl\_sites = example.com\*2, example.net, example.org

```

 To filter only DNSBL replies containing 127.0.0.4: 



```

postscreen\_dnsbl\_sites = example.com=127.0.0.4

```

 This feature is available in Postfix 2.8. 


