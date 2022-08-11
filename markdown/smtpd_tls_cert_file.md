# smtpd_tls_cert_file (default: empty)
 File with the Postfix SMTP server RSA certificate in PEM format.
This file may also contain the Postfix SMTP server private RSA key.
With Postfix ≥ 3.4 the preferred way to configure server keys and
certificates is via the "smtpd\_tls\_chain\_files" parameter. 


 Public Internet MX hosts without certificates signed by a "reputable"
CA must generate, and be prepared to present to most clients, a
self-signed or private-CA signed certificate. The client will not be
able to authenticate the server, but unless it is running Postfix 2.3 or
similar software, it will still insist on a server certificate. 


 For servers that are **not** public Internet MX hosts, Postfix
supports configurations with no certificates. This entails the use of
just the anonymous TLS ciphers, which are not supported by typical SMTP
clients. Since some clients may not fall back to plain text after a TLS
handshake failure, a certificate-less Postfix SMTP server will be unable
to receive email from some TLS-enabled clients. To avoid accidental
configurations with no certificates, Postfix enables certificate-less
operation only when the administrator explicitly sets
"smtpd\_tls\_cert\_file = none". This ensures that new Postfix SMTP server
configurations will not accidentally enable TLS without certificates. 


 Note that server certificates are not optional in TLS 1.3. To run
without certificates you'd have to disable the TLS 1.3 protocol by
including '!TLSv1.3' in "smtpd\_tls\_protocols" and perhaps also
"smtpd\_tls\_mandatory\_protocols". It is simpler instead to just
configure a certificate chain. Certificate-less operation is not
recommended. 




 Both RSA and DSA certificates are supported. When both types
are present, the cipher used determines which certificate will be
presented to the client. For Netscape and OpenSSL clients without
special cipher choices the RSA certificate is preferred. 


 To enable a remote SMTP client to verify the Postfix SMTP server
certificate, the issuing CA certificates must be made available to the
client. You should include the required certificates in the server
certificate file, the server certificate first, then the issuing
CA(s) (bottom-up order). 


 Example: the certificate for "server.example.com" was issued by
"intermediate CA" which itself has a certificate of "root CA".
Create the server.pem file with "cat server\_cert.pem intermediate\_CA.pem
root\_CA.pem > server.pem". 


 If you also want to verify client certificates issued by these
CAs, you can add the CA certificates to the smtpd\_tls\_CAfile, in which
case it is not necessary to have them in the smtpd\_tls\_cert\_file,
smtpd\_tls\_dcert\_file (obsolete) or smtpd\_tls\_eccert\_file. 


 A certificate supplied here must be usable as an SSL server certificate
and hence pass the "openssl verify -purpose sslserver ..." test. 


 Example: 



```

smtpd\_tls\_cert\_file = /etc/postfix/server.pem

```

 This feature is available in Postfix 2.2 and later. 


