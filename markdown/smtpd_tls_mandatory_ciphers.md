# smtpd_tls_mandatory_ciphers (default: medium)
 The minimum TLS cipher grade that the Postfix SMTP server will
use with mandatory TLS encryption. The default grade ("medium") is
sufficiently strong that any benefit from globally restricting TLS
sessions to a more stringent grade is likely negligible, especially
given the fact that many implementations still do not offer any stronger
("high" grade) ciphers, while those that do, will always use "high"
grade ciphers. So insisting on "high" grade ciphers is generally
counter-productive. Allowing "export" or "low" ciphers is typically
not a good idea, as systems limited to just these are limited to
obsolete browsers. No known SMTP clients fail to support at least
one "medium" or "high" grade cipher. 


 The following cipher grades are supported: 



**export**
 Enable "EXPORT" grade or stronger OpenSSL ciphers. The
underlying cipherlist is specified via the tls\_export\_cipherlist
configuration parameter, which you are strongly encouraged not to
change. This choice is insecure and SHOULD NOT be used. 
**low**
 Enable "LOW" grade or stronger OpenSSL ciphers. The underlying
cipherlist is specified via the tls\_low\_cipherlist configuration
parameter, which you are strongly encouraged not to change. This
choice is insecure and SHOULD NOT be used. 
**medium**
 Enable "MEDIUM" grade or stronger OpenSSL ciphers. These use 128-bit
or longer symmetric bulk-encryption keys. This is the default minimum
strength for mandatory TLS encryption. The underlying cipherlist is
specified via the tls\_medium\_cipherlist configuration parameter, which
you are strongly encouraged not to change. 
**high**
 Enable only "HIGH" grade OpenSSL ciphers. The
underlying cipherlist is specified via the tls\_high\_cipherlist
configuration parameter, which you are strongly encouraged to
not change. 
**null**
 Enable only the "NULL" OpenSSL ciphers, these provide authentication
without encryption. This setting is only appropriate in the rare
case that all clients are prepared to use NULL ciphers (not normally
enabled in TLS clients). The underlying cipherlist is specified via the
tls\_null\_cipherlist configuration parameter, which you are strongly
encouraged not to change. 

 Cipher types listed in
smtpd\_tls\_mandatory\_exclude\_ciphers or smtpd\_tls\_exclude\_ciphers are
excluded from the base definition of the selected cipher grade. See
smtpd\_tls\_ciphers for cipher controls that apply to opportunistic
TLS. 


 The underlying cipherlists for grades other than "null" include
anonymous ciphers, but these are automatically filtered out if the
server is configured to ask for remote SMTP client certificates. You are very
unlikely to need to take any steps to exclude anonymous ciphers, they
are excluded automatically as required. If you must exclude anonymous
ciphers even when Postfix does not need or use peer certificates, set
"smtpd\_tls\_exclude\_ciphers = aNULL". To exclude anonymous ciphers only
when TLS is enforced, set "smtpd\_tls\_mandatory\_exclude\_ciphers = aNULL". 


 This feature is available in Postfix 2.3 and later. 


