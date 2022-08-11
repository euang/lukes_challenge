# tls_disable_workarounds (default: see "postconf -d" output)
 List or bit-mask of OpenSSL bug work-arounds to disable. 


 The OpenSSL toolkit includes a set of work-arounds for buggy SSL/TLS
implementations. Applications, such as Postfix, that want to maximize
interoperability ask the OpenSSL library to enable the full set of
recommended work-arounds. 


 From time to time, it is discovered that a work-around creates a
security issue, and should no longer be used. If upgrading OpenSSL
to a fixed version is not an option or an upgrade is not available
in a timely manner, or in closed environments where no buggy clients
or servers exist, it may be appropriate to disable some or all of the
OpenSSL interoperability work-arounds. This parameter specifies which
bug work-arounds to disable. 


 If the value of the parameter is a hexadecimal long integer starting
with "0x", the bug work-arounds corresponding to the bits specified in
its value are removed from the **SSL\_OP\_ALL** work-around bit-mask
(see openssl/ssl.h and SSL\_CTX\_set\_options(3)). You can specify more
bits than are present in SSL\_OP\_ALL, excess bits are ignored. Specifying
0xFFFFFFFF disables all bug-workarounds on a 32-bit system. This should
also be sufficient on 64-bit systems, until OpenSSL abandons support
for 32-bit systems and starts using the high 32 bits of a 64-bit
bug-workaround mask. 


 Otherwise, the parameter is a white-space or comma separated list
of specific named bug work-arounds chosen from the list below. It
is possible that your OpenSSL version includes new bug work-arounds
added after your Postfix source code was last updated, in that case
you can only disable one of these via the hexadecimal syntax above. 



**CRYPTOPRO\_TLSEXT\_BUG** New with GOST support in
OpenSSL 1.0.0.
**DONT\_INSERT\_EMPTY\_FRAGMENTS** See
SSL\_CTX\_set\_options(3)
**LEGACY\_SERVER\_CONNECT** See SSL\_CTX\_set\_options(3)
**MICROSOFT\_BIG\_SSLV3\_BUFFER** See
SSL\_CTX\_set\_options(3)
**MICROSOFT\_SESS\_ID\_BUG** See SSL\_CTX\_set\_options(3)
**MSIE\_SSLV2\_RSA\_PADDING**  also aliased as
**CVE-2005-2969**. Postfix 2.8 disables this work-around by
default with OpenSSL versions that may predate the fix. Fixed in
OpenSSL 0.9.7h and OpenSSL 0.9.8a.
**NETSCAPE\_CHALLENGE\_BUG** See SSL\_CTX\_set\_options(3)
**NETSCAPE\_REUSE\_CIPHER\_CHANGE\_BUG**  also aliased
as **CVE-2010-4180**. Postfix 2.8 disables this work-around by
default with OpenSSL versions that may predate the fix. Fixed in
OpenSSL 0.9.8q and OpenSSL 1.0.0c.
**SSLEAY\_080\_CLIENT\_DH\_BUG** See
SSL\_CTX\_set\_options(3)
**SSLREF2\_REUSE\_CERT\_TYPE\_BUG** See
SSL\_CTX\_set\_options(3)
**TLS\_BLOCK\_PADDING\_BUG** See SSL\_CTX\_set\_options(3)
**TLS\_D5\_BUG** See SSL\_CTX\_set\_options(3)
**TLS\_ROLLBACK\_BUG** See SSL\_CTX\_set\_options(3).
This is disabled in OpenSSL 0.9.7 and later. Nobody should still
be using 0.9.6! 
**TLSEXT\_PADDING**Postfix ≥ 3.4. See SSL\_CTX\_set\_options(3).

 This feature is available in Postfix 2.8 and later. 


