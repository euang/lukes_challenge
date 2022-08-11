# tls_dane_digests (default: sha512 sha256)
 DANE TLSA (RFC 6698, RFC 7671, RFC 7672) resource-record "matching
type" digest algorithms in descending preference order. All the
specified algorithms must be supported by the underlying OpenSSL
library, otherwise the Postfix SMTP client will not support DANE
TLSA security. 


 Specify a list of digest names separated by commas and/or
whitespace. Each digest name may be followed by an optional
"=<number>" suffix. For example, "sha512" may instead be specified
as "sha512=2" and "sha256" may instead be specified as "sha256=1".
The optional number must match the IANA assigned TLSA matching type number the algorithm in question.
Postfix will check this constraint for the algorithms it knows about.
Additional matching type algorithms registered with IANA can be added
with explicit numbers provided they are supported by OpenSSL. 


 Invalid list elements are logged with a warning and disable DANE
support. TLSA RRs that specify digests not included in the list are
ignored with a warning. 


 Note: It is unwise to omit sha256 from the digest list. This
digest algorithm is the only mandatory to implement digest algorithm
in RFC 6698, and many servers are expected to publish TLSA records
with just sha256 digests. Unless one of the standard digests is
seriously compromised and servers have had ample time to update their
TLSA records you should not omit any standard digests, just arrange
them in order from strongest to weakest. 


 This feature is available in Postfix 2.11 and later. 


