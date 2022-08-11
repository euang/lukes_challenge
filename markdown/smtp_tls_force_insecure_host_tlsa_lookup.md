# smtp_tls_force_insecure_host_tlsa_lookup (default: no)
 Lookup the associated DANE TLSA RRset even when a hostname is
not an alias and its address records lie in an unsigned zone. This
is unlikely to ever yield DNSSEC validated results, since child
zones of unsigned zones are also unsigned in the absence of DLV or
locally configured non-root trust-anchors. We anticipate that such
mechanisms will not be used for just the "\_tcp" subdomain of a host.
Suppressing the TLSA RRset lookup reduces latency and avoids potential
interoperability problems with nameservers for unsigned zones that
are not prepared to handle the new TLSA RRset. 


 This feature is available in Postfix 2.11. 


