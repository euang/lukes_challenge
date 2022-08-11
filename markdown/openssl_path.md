# openssl_path (default: openssl)

The location of the OpenSSL command line program openssl(1). This
is used by the "**postfix tls**" command to create private keys,
certificate signing requests, self-signed certificates, and to
compute public key digests for DANE TLSA records. In multi-instance
environments, this parameter is always determined from the configuration
of the default Postfix instance.



 Example: 



> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     # NetBSD pkgsrc:
>     openssl\_path = /usr/pkg/bin/openssl
>     # Local build:
>     openssl\_path = /usr/local/bin/openssl
> 
> ```
> 
> 



This feature is available in Postfix 3.1 and later.



