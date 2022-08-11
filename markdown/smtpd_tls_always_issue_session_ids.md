# smtpd_tls_always_issue_session_ids (default: yes)
 Force the Postfix SMTP server to issue a TLS session id, even
when TLS session caching is turned off (smtpd\_tls\_session\_cache\_database
is empty). This behavior is compatible with Postfix < 2.3. 


 With Postfix 2.3 and later the Postfix SMTP server can disable
session id generation when TLS session caching is turned off. This
keeps remote SMTP clients from caching sessions that almost certainly cannot
be re-used. 


 By default, the Postfix SMTP server always generates TLS session
ids. This works around a known defect in mail client applications
such as MS Outlook, and may also prevent interoperability issues
with other MTAs. 


 Example: 



```

smtpd\_tls\_always\_issue\_session\_ids = no

```

 This feature is available in Postfix 2.3 and later. 


