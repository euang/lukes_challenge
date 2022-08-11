# send_cyrus_sasl_authzid (default: no)
 When authenticating to a remote SMTP or LMTP server with the
default setting "no", send no SASL authoriZation ID (authzid); send
only the SASL authentiCation ID (authcid) plus the authcid's password.



 The non-default setting "yes" enables the behavior of older
Postfix versions. These always send a SASL authzid that is equal
to the SASL authcid, but this causes interoperability problems
with some SMTP servers. 


 This feature is available in Postfix 2.4.4 and later. 


