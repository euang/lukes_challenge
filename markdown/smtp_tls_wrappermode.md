# smtp_tls_wrappermode (default: no)
 Request that the Postfix SMTP client connects using the
SUBMISSIONS/SMTPS protocol instead of using the STARTTLS command. 


 This mode requires "smtp\_tls\_security\_level = encrypt" or
stronger. 


 Example: deliver all remote mail via a provider's server
"mail.example.com". 



```

/etc/postfix/main.cf:
    # Client-side SMTPS requires "encrypt" or stronger.
    smtp\_tls\_security\_level = encrypt
    smtp\_tls\_wrappermode = yes
    # The [] suppress MX lookups.
    relayhost = [mail.example.com]:465

```

 More examples are in TLS\_README, including examples for older
Postfix versions. 


 This feature is available in Postfix 3.0 and later. 


