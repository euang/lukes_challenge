# smtp_tls_trust_anchor_file (default: empty)
 Zero or more PEM-format files with trust-anchor certificates
and/or public keys. If the parameter is not empty the root CAs in
CAfile and CApath are no longer trusted. Rather, the Postfix SMTP
client will only trust certificate-chains signed by one of the
trust-anchors contained in the chosen files. The specified
trust-anchor certificates and public keys are not subject to
expiration, and need not be (self-signed) root CAs. They may, if
desired, be intermediate certificates. Therefore, these certificates
also may be found "in the middle" of the trust chain presented by
the remote SMTP server, and any untrusted issuing parent certificates
will be ignored. Specify a list of pathnames separated by comma
or whitespace. 


 Whether specified in main.cf, or on a per-destination basis,
the trust-anchor PEM file must be accessible to the Postfix SMTP
client in the chroot jail if applicable. The trust-anchor file
should contain only certificates and public keys, no private key
material, and must be readable by the non-privileged $mail\_owner
user. This allows destinations to be bound to a set of specific
CAs or public keys without trusting the same CAs for all destinations.



 The main.cf parameter supports single-purpose Postfix installations
that send mail to a fixed set of SMTP peers. At most sites, if
trust-anchor files are used at all, they will be specified on a
per-destination basis via the "tafile" attribute of the "verify"
and "secure" levels in smtp\_tls\_policy\_maps. 


 The underlying mechanism is in support of RFC 7672 (DANE TLSA),
which defines mechanisms for an SMTP client MTA to securely determine
server TLS certificates via DNS. 


 If you want your trust anchors to be public keys, with OpenSSL
you can extract a single PEM public key from a PEM X.509 file
containing a single certificate, as follows: 



> 
> 
> ```
> 
> $ openssl x509 -in cert.pem -out ta-key.pem -noout -pubkey
> 
> ```
> 
> 


 This feature is available in Postfix 2.11 and later. 


