# tls_preempt_cipherlist (default: no)
 With SSLv3 and later, use the Postfix SMTP server's cipher
preference order instead of the remote client's cipher preference
order. 


 By default, the OpenSSL server selects the client's most preferred
cipher that the server supports. With SSLv3 and later, the server may
choose its own most preferred cipher that is supported (offered) by
the client. Setting "tls\_preempt\_cipherlist = yes" enables server cipher
preferences. 


 While server cipher selection may in some cases lead to a more secure
or performant cipher choice, there is some risk of interoperability
issues. In the past, some SSL clients have listed lower priority ciphers
that they did not implement correctly. If the server chooses a cipher
that the client prefers less, it may select a cipher whose client
implementation is flawed. Most notably Windows 2003 Microsoft
Exchange servers have flawed implementations of DES-CBC3-SHA, which
OpenSSL considers stronger than RC4-SHA. Enabling server cipher-suite
selection may create interoperability issues with Windows 2003
Microsoft Exchange clients. 


 This feature is available in Postfix 2.8 and later, in combination
with OpenSSL 0.9.7 and later. 


