# smtp_tls_cipherlist (default: empty)
 Obsolete Postfix < 2.3 control for the Postfix SMTP client TLS
cipher list. As this feature applies to all TLS security levels, it is easy
to create interoperability problems by choosing a non-default cipher
list. Do not use a non-default TLS cipher list on hosts that deliver email
to the public Internet: you will be unable to send email to servers that
only support the ciphers you exclude. Using a restricted cipher list
may be more appropriate for an internal MTA, where one can exert some
control over the TLS software and settings of the peer servers. 


 **Note:** do not use "" quotes around the parameter value. 


 This feature is available in Postfix version 2.2. It is not used with
Postfix 2.3 and later; use smtp\_tls\_mandatory\_ciphers instead. 


