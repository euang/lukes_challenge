# smtp_tls_mandatory_exclude_ciphers (default: empty)
 Additional list of ciphers or cipher types to exclude from the
Postfix SMTP client cipher list at mandatory TLS security levels. This list
works in addition to the exclusions listed with smtp\_tls\_exclude\_ciphers
(see there for syntax details). 


 Starting with Postfix 2.6, the mandatory cipher exclusions can be
specified on a per-destination basis via the TLS policy "exclude"
attribute. See smtp\_tls\_policy\_maps for notes and examples. 


 This feature is available in Postfix 2.3 and later. 


