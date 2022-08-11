# tls_eecdh_strong_curve (default: prime256v1)
 The elliptic curve used by the Postfix SMTP server for sensibly
strong
ephemeral ECDH key exchange. This curve is used by the Postfix SMTP
server when "smtpd\_tls\_eecdh\_grade = strong". The phrase "sensibly
strong" means approximately 128-bit security based on best known
attacks. The selected curve must be implemented by OpenSSL (as
reported by ecparam(1) with the "-list\_curves" option) and be one
of the curves listed in Section 5.1.1 of RFC 8422. You should not
generally change this setting. Remote SMTP client implementations
must support this curve for EECDH key exchange to take place. It
is unwise to choose only "bleeding-edge" curves supported by only a
small subset of clients. 


 The default "strong" curve is rated in NSA Suite
B for information classified up to SECRET. 


 Note: elliptic curve names are poorly standardized; different
standards groups are assigning different names to the same underlying
curves. The curve with the X9.62 name "prime256v1" is also known
under the SECG name "secp256r1", but OpenSSL does not recognize the
latter name. 


 If you want to take maximal advantage of ciphers that offer forward secrecy see
the Getting
started section of FORWARD\_SECRECY\_README. The
full document conveniently presents all information about Postfix
"perfect" forward secrecy support in one place: what forward secrecy
is, how to tweak settings, and what you can expect to see when
Postfix uses ciphers with forward secrecy. 


 This feature is available in Postfix 2.6 and later, when it is
compiled and linked with OpenSSL 1.0.0 or later on platforms where
EC algorithms have not been disabled by the vendor. 


