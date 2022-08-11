# smtp_tls_cert_file (default: empty)
 File with the Postfix SMTP client RSA certificate in PEM format.
This file may also contain the Postfix SMTP client private RSA key, and
these may be the same as the Postfix SMTP server RSA certificate and key
file. With Postfix ≥ 3.4 the preferred way to configure client keys
and certificates is via the "smtp\_tls\_chain\_files" parameter. 


 Do not configure client certificates unless you **must** present
client TLS certificates to one or more servers. Client certificates are
not usually needed, and can cause problems in configurations that work
well without them. The recommended setting is to let the defaults stand: 



> 
> 
> ```
> 
> smtp\_tls\_cert\_file =
> smtp\_tls\_key\_file =
> smtp\_tls\_eccert\_file =
> smtp\_tls\_eckey\_file =
> # Obsolete DSA parameters
> smtp\_tls\_dcert\_file =
> smtp\_tls\_dkey\_file =
> # Postfix ≥ 3.4 interface
> smtp\_tls\_chain\_files =
> 
> ```
> 
> 


 The best way to use the default settings is to comment out the above
parameters in main.cf if present. 


 To enable remote SMTP servers to verify the Postfix SMTP client
certificate, the issuing CA certificates must be made available to the
server. You should include the required certificates in the client
certificate file, the client certificate first, then the issuing
CA(s) (bottom-up order). 


 Example: the certificate for "client.example.com" was issued by
"intermediate CA" which itself has a certificate issued by "root CA".
As the "root" super-user create the client.pem file with: 



> 
> 
> ```
> 
> # **umask 077**
> # **cat client\_key.pem client\_cert.pem intermediate\_CA.pem > chain.pem** 
> 
> ```
> 
> 


 If you also want to verify remote SMTP server certificates issued by
these CAs, you can add the CA certificates to the smtp\_tls\_CAfile, in
which case it is not necessary to have them in the smtp\_tls\_cert\_file,
smtp\_tls\_dcert\_file (obsolete) or smtp\_tls\_eccert\_file. 


 A certificate supplied here must be usable as an SSL client certificate
and hence pass the "openssl verify -purpose sslclient ..." test. 


 Example: 



```

smtp\_tls\_cert\_file = /etc/postfix/chain.pem

```

 This feature is available in Postfix 2.2 and later. 


