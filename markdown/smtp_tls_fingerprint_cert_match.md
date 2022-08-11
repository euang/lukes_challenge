# smtp_tls_fingerprint_cert_match (default: empty)
 List of acceptable remote SMTP server certificate fingerprints for
the "fingerprint" TLS security level (**smtp\_tls\_security\_level** =
fingerprint). At this security level, Certification Authorities are not
used, and certificate expiration times are ignored. Instead, server
certificates are verified directly via their certificate fingerprint
or public key fingerprint (Postfix 2.9 and later). The fingerprint
is a message digest of the server certificate (or public key). The
digest algorithm is selected via the **smtp\_tls\_fingerprint\_digest**
parameter. 


 The colons between each pair of nibbles in the fingerprint value
are optional (Postfix ≥ 3.6). These were required in earlier
Postfix releases. 


 When an **smtp\_tls\_policy\_maps** table entry specifies the
"fingerprint" security level, any "match" attributes in that entry specify
the list of valid fingerprints for the corresponding destination. Multiple
fingerprints can be combined with a "|" delimiter in a single match
attribute, or multiple match attributes can be employed. 


 Example: Certificate fingerprint verification with internal mailhub.
Two matching fingerprints are listed. The relayhost may be multiple
physical hosts behind a load-balancer, each with its own private/public
key and self-signed certificate. Alternatively, a single relayhost may
be in the process of switching from one set of private/public keys to
another, and both keys are trusted just prior to the transition. 



> 
> 
> ```
> 
> relayhost = [mailhub.example.com]
> smtp\_tls\_security\_level = fingerprint
> smtp\_tls\_fingerprint\_digest = sha256
> smtp\_tls\_fingerprint\_cert\_match =
>     cd:fc:d8:db:f8:c4:82:96:6c:...:28:71:e8:f5:8d:a5:0d:9b:d4:a6
>     dd:5c:ef:f5:c3:bc:64:25:36:...:99:36:06:ce:40:ef:de:2e:ad:a4
> 
> ```
> 
> 


 Example: Certificate fingerprint verification with selected destinations.
As in the example above, we show two matching fingerprints: 



> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     smtp\_tls\_policy\_maps = hash:/etc/postfix/tls\_policy
>     smtp\_tls\_fingerprint\_digest = sha256
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/tls\_policy:
>     example.com fingerprint
>         match=51:e9:af:2e:1e:40:1f:...:64:0a:30:35:2d:09:16:31:5a:eb:82:76
>         match=b6:b4:72:34:e2:59:cd:...:c2:ca:63:0d:4d:cc:2c:7d:84:de:e6:2f
> 
> ```
> 
> 


 This feature is available in Postfix 2.5 and later. 


