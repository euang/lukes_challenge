# tls_server_sni_maps (default: empty)
 Optional lookup tables that map names received from remote SMTP
clients via the TLS Server Name Indication (SNI) extension to the
appropriate keys and certificate chains. This parameter is implemented
in the Postfix TLS library, and applies to both smtpd(8) and the SMTP
server mode of tlsproxy(8). 


 When this parameter is non-empty, the Postfix SMTP server enables
SNI extension processing, and logs SNI values that are invalid or
don't match an entry in the specified tables. When an entry
does match, the SNI name is logged as part of the connection summary
at log levels 1 and higher. 


 The lookup key is either the verbatim SNI domain name or an
ancestor domain prefixed with a leading dot. For internationalized
domains, the lookup key must be in IDNA 2008 A-label form (as
required in the TLS SNI extension). 


 The syntax of the lookup value is the same as with the
smtp\_tls\_chain\_files parameter (see there for additional details),
but here scoped to just TLS connections in which the client sends
a matching SNI domain name. 


 Example: 



> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     #
>     # The indexed SNI table must be created with "postmap -F"
>     #
>     indexed = ${default\_database\_type}:${config\_directory}/
>     tls\_server\_sni\_maps = ${indexed}sni
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/sni:
>     #
>     # The example.com domain has both an RSA and ECDSA certificate
>     # chain.  The chain files MUST start with the private key,
>     # with the certificate chain next, starting with the leaf
>     # (server) certificate, and then the issuer certificates.
>     #
>     example.com /etc/postfix/sni-chains/rsa2048.example.com.pem,
>                 /etc/postfix/sni-chains/ecdsa-p256.example.com.pem
>     #
>     # The example.net domain has a wildcard certificate, and two
>     # additional DNS names.  So its certificate chain is also used
>     # with any subdomain, plus the additional names.
>     #
>     example.net /etc/postfix/sni-chains/example.net.pem
>     .example.net /etc/postfix/sni-chains/example.net.pem
>     example.info /etc/postfix/sni-chains/example.net.pem
>     example.org /etc/postfix/sni-chains/example.net.pem
> 
> ```
> 
> 


 Note that the SNI lookup tables should also have entries for
the domains that correspond to the Postfix SMTP server's default
certificate(s). This ensures that the remote SMTP client's TLS SNI
extension gets a positive response when it specifies one of the
Postfix SMTP server's default domains, and ensures that the Postfix
SMTP server will not log an SNI name mismatch for such a domain.
The Postfix SMTP server's default certificates are then only used
when the client sends no SNI or when it sends SNI with a domain
that the server knows no certificate(s) for. 


 The mapping from an SNI domain name to a certificate chain is indirect. In
the input source files for "cdb", "hash", "btree" or other tables that are
converted to on-disk indexed files via postmap(1), the value specified for each
key is a list of filenames. When postmap(1) is used with the **-F** option,
the generated table stores for each lookup key the base64-encoded contents of
the associated files. When querying tables via **postmap -Fq**, the table
value is decoded from base64, yielding the original file content, plus a new
line. 


 With "regexp", "pcre", "inline", "texthash", "static" and similar
tables that are interpreted at run-time, and don't have a separate
source format, the table value is again a list files, that are loaded
into memory when the table is opened. 


 With tables whose content is managed outside of Postfix, such
as LDAP, MySQL, PostgreSQL, socketmap and tcp, the value must be a
concatenation of the desired PEM keys and certificate chains, that
is then further encoded to yield a single-line base64 string.
Creation of such tables and secure storage (the value includes
private key material) are outside the responsibility of Postfix. 


 With "socketmap" and "tcp" the data will be transmitted in the clear, and
there is no query access control, so these are generally unsuitable for storing
SNI chains. With LDAP and SQL, you should restrict read access and use TLS to
protect the sensitive data in transit. 


 Typically there is only one private key and its chain of certificates
starting with the "leaf" certificate corresponding to that key, and
continuing with the appropriate intermediate issuer CA certificates,
with each certificate ideally followed by its issuer. Servers
that have keys and certificates for more than one algorithm (e.g.
both an RSA key and an ECDSA key, or even RSA, ECDSA and Ed25519)
can use multiple chains concatenated together, with the key always
listed before the corresponding certificates. 


 This feature is available in Postfix 3.4 and later. 


