# fast_flush_domains (default: $relay_domains)

Optional list of destinations that are eligible for per-destination
logfiles with mail that is queued to those destinations.




By default, Postfix maintains "fast flush" logfiles only for
destinations that the Postfix SMTP server is willing to relay to
(i.e. the default is: "fast\_flush\_domains = $relay\_domains"; see
the relay\_domains parameter in the postconf(5) manual).



 Specify a list of hosts or domains, "/file/name" patterns or
"type:table" lookup tables, separated by commas and/or whitespace.
Continue long lines by starting the next line with whitespace. A
"/file/name" pattern is replaced by its contents; a "type:table"
lookup table is matched when the domain or its parent domain appears
as lookup key. 


 Pattern matching of domain names is controlled by the presence
or absence of "fast\_flush\_domains" in the parent\_domain\_matches\_subdomains
parameter value. 



Specify "fast\_flush\_domains =" (i.e., empty) to disable the feature
altogether.



