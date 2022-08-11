# smtp_tls_scert_verifydepth (default: 9)
 The verification depth for remote SMTP server certificates. A depth
of 1 is sufficient if the issuing CA is listed in a local CA file. 


 The default verification depth is 9 (the OpenSSL default) for
compatibility with earlier Postfix behavior. Prior to Postfix 2.5,
the default value was 5, but the limit was not actually enforced. If
you have set this to a lower non-default value, certificates with longer
trust chains may now fail to verify. Certificate chains with 1 or 2
CAs are common, deeper chains are more rare and any number between 5
and 9 should suffice in practice. You can choose a lower number if,
for example, you trust certificates directly signed by an issuing CA
but not any CAs it delegates to. 


 This feature is available in Postfix 2.2 and later. 


