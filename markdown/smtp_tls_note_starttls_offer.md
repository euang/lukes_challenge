# smtp_tls_note_starttls_offer (default: no)
 Log the hostname of a remote SMTP server that offers STARTTLS,
when TLS is not already enabled for that server. 


 The logfile record looks like: 



```

postfix/smtp[pid]:  Host offered STARTTLS: [name.of.host]

```

 This feature is available in Postfix 2.2 and later. 


