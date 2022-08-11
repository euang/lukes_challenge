# tls_eecdh_auto_curves (default: see "postconf -d" output)
 The prioritized list of elliptic curves supported by the Postfix
SMTP client and server. These curves are used by the Postfix SMTP
server when "smtpd\_tls\_eecdh\_grade = auto". The selected curves
must be implemented by OpenSSL and be standardized for use in TLS
(RFC 8422). It is unwise to list only
"bleeding-edge" curves supported by a small subset of clients. The
default list is suitable for most users. 


 Postfix skips curve names that are unknown to OpenSSL, or that
are known but not yet implemented. This makes it possible to
"anticipate" support for curves that should be used once they become
available. In particular, in some OpenSSL versions, the new RFC
8031 curves "X25519" and "X448" may be known by name, but ECDH
support for either or both may be missing. These curves may appear
in the default value of this parameter, even though they'll only
be usable with later versions of OpenSSL. 


 This feature is available in Postfix 3.2 and later, when it is
compiled and linked with OpenSSL 1.0.2 or later on platforms where
EC algorithms have not been disabled by the vendor. 


