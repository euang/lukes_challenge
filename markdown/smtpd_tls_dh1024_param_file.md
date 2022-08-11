# smtpd_tls_dh1024_param_file (default: empty)
 File with DH parameters that the Postfix SMTP server should
use with non-export EDH ciphers. 


 With Postfix ≥ 3.7, built with OpenSSL version is 3.0.0 or later, if the
parameter value is either empty or "**auto**", then the DH parameter
selection is delegated to the OpenSSL library, which selects appropriate
parameters based on the TLS handshake. This choice is likely to be the most
interoperable with SMTP clients using various TLS libraries, and custom local
parameters are no longer recommended when using Postfix ≥ 3.7 built against
OpenSSL 3.0.0. 


 The best-practice choice of parameters uses a 2048-bit prime. This is fine,
despite the historical "1024" in the parameter name. Do not be tempted to use
much larger values, performance degrades quickly, and you may also cease to
interoperate with some mainstream SMTP clients. As of Postfix 3.1, the
compiled-in default prime is 2048-bits, and it is not strictly necessary,
though perhaps somewhat beneficial to generate custom DH parameters. 


 Instead of using the exact same parameter sets as distributed
with other TLS packages, it is more secure to generate your own
set of parameters with something like the following commands: 



> 
> 
> ```
> 
> openssl dhparam -out /etc/postfix/dh2048.pem 2048
> openssl dhparam -out /etc/postfix/dh1024.pem 1024
> # As of Postfix 3.6, export-grade 512-bit DH parameters are no longer
> # supported or needed.
> openssl dhparam -out /etc/postfix/dh512.pem 512
> 
> ```
> 
> 


 It is safe to share the same DH parameters between multiple
Postfix instances. If you prefer, you can generate separate
parameters for each instance. 


 If you want to take maximal advantage of ciphers that offer forward secrecy see
the Getting
started section of FORWARD\_SECRECY\_README. The
full document conveniently presents all information about Postfix
"perfect" forward secrecy support in one place: what forward secrecy
is, how to tweak settings, and what you can expect to see when
Postfix uses ciphers with forward secrecy. 


 Example: 



```

smtpd\_tls\_dh1024\_param\_file = /etc/postfix/dh2048.pem

```

This feature is available in Postfix 2.2 and later.


