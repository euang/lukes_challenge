# milter_header_checks (default: empty)
 Optional lookup tables for content inspection of message headers
that are produced by Milter applications. See the header\_checks(5)
manual page available actions. Currently, PREPEND is not implemented.



 The following example sends all mail that is marked as SPAM to
a spam handling machine. Note that matches are case-insensitive
by default. 



```

/etc/postfix/main.cf:
    milter\_header\_checks = pcre:/etc/postfix/milter\_header\_checks

```


```

/etc/postfix/milter\_header\_checks:
    /^X-SPAM-FLAG:\s+YES/ FILTER mysmtp:sanitizer.example.com:25

```

 The milter\_header\_checks mechanism could also be used for
allowlisting. For example it could be used to skip heavy content
inspection for DKIM-signed mail from known friendly domains. 


 This feature is available in Postfix 2.7, and as an optional
patch for Postfix 2.6. 


