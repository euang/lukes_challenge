# tls_ssl_options (default: empty)
 List or bit-mask of OpenSSL options to enable. 


 The OpenSSL toolkit provides a set of options that applications
can enable to tune the OpenSSL behavior. Some of these work around
bugs in other implementations and are on by default. You can use
the tls\_disable\_workarounds parameter to selectively disable some
or all of the bug work-arounds, making OpenSSL more strict at the
cost of non-interoperability with SSL clients or servers that exhibit
the bugs. 


 Other options are off by default, and typically enable or disable
features rather than bug work-arounds. These may be turned on (with
care) via the tls\_ssl\_options parameter. The value is a white-space
or comma separated list of named options chosen from the list below.
The names are not case-sensitive, you can use lower-case if you
prefer. The upper case values below match the corresponding macro
name in the ssl.h header file with the SSL\_OP\_ prefix removed. It
is possible that your OpenSSL version includes new options added
after your Postfix source code was last updated, in that case you
can only enable one of these via the hexadecimal syntax below. 


 You should only enable features via the hexadecimal mask when
the need to control the feature is critical (to deal with a new
vulnerability or a serious interoperability problem). Postfix DOES
NOT promise backwards compatible behavior with respect to the mask
bits. A feature enabled via the mask in one release may be enabled
by other means in a later release, and the mask bit will then be
ignored. Therefore, use of the hexadecimal mask is only a temporary
measure until a new Postfix or OpenSSL release provides a better
solution. 


 If the value of the parameter is a hexadecimal long integer
starting with "0x", the options corresponding to the bits specified
in its value are enabled (see openssl/ssl.h and SSL\_CTX\_set\_options(3)).
You can only enable options not already controlled by other Postfix
settings. For example, you cannot disable protocols or enable
server cipher preference. Do not attempt to enable all features by
specifying 0xFFFFFFFF, this is unlikely to be a good idea. Some
bug work-arounds are also valid here, allowing them to be re-enabled
if/when they're no longer enabled by default. The supported values
include: 



**ENABLE\_MIDDLEBOX\_COMPAT** Postfix ≥ 3.4. See
SSL\_CTX\_set\_options(3).
**LEGACY\_SERVER\_CONNECT** See SSL\_CTX\_set\_options(3).
**NO\_TICKET** Enabled by default when needed in
fully-patched Postfix ≥ 2.7. Not needed at all for Postfix ≥
2.11, unless for some reason you do not want to support TLS session
resumption. Best not set explicitly. See SSL\_CTX\_set\_options(3).
**NO\_COMPRESSION** Disable SSL compression even if
supported by the OpenSSL library. Compression is CPU-intensive,
and compression before encryption does not always improve security. 
**NO\_RENEGOTIATION** Postfix ≥ 3.4. This can
reduce opportunities for a potential CPU exhaustion attack. See
SSL\_CTX\_set\_options(3).
**NO\_SESSION\_RESUMPTION\_ON\_RENEGOTIATION** Postfix
≥ 3.4. See SSL\_CTX\_set\_options(3).
**PRIORITIZE\_CHACHA** Postfix ≥ 3.4. See SSL\_CTX\_set\_options(3).

 This feature is available in Postfix 2.11 and later. 


