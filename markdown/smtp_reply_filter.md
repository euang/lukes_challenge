# smtp_reply_filter (default: empty)
 A mechanism to transform replies from remote SMTP servers one
line at a time. This is a last-resort tool to work around server
replies that break interoperability with the Postfix SMTP client.
Other uses involve fault injection to test Postfix's handling of
invalid responses. 


 Notes: 


* In the case of a multi-line reply, the Postfix SMTP client
uses the final reply line's numerical SMTP reply code and enhanced
status code.
* The numerical SMTP reply code (XYZ) takes precedence over
the enhanced status code (X.Y.Z). When the enhanced status code
initial digit differs from the SMTP reply code initial digit, or
when no enhanced status code is present, the Postfix SMTP client
uses a generic enhanced status code (X.0.0) instead.


 Specify the name of a "type:table" lookup table. The search
string is a single SMTP reply line as received from the remote SMTP
server, except that the trailing <CR><LF> are removed.
When the lookup succeeds, the result replaces the single SMTP reply
line. 


 Examples: 



```

/etc/postfix/main.cf:
    smtp\_reply\_filter = pcre:/etc/postfix/reply\_filter

```


```

/etc/postfix/reply\_filter:
    # Transform garbage into "250-filler..." so that it looks like
    # one line from a multi-line reply. It does not matter what we
    # substitute here as long it has the right syntax.  The Postfix
    # SMTP client will use the final line's numerical SMTP reply
    # code and enhanced status code.
    !/^([2-5][0-9][0-9]($|[- ]))/ 250-filler for garbage

```

 This feature is available in Postfix 2.7. 


