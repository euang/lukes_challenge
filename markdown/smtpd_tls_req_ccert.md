# smtpd_tls_req_ccert (default: no)
 With mandatory TLS encryption, require a trusted remote SMTP client
certificate in order to allow TLS connections to proceed. This
option implies "smtpd\_tls\_ask\_ccert = yes". 


 When TLS encryption is optional, this setting is ignored with
a warning written to the mail log. 


 This feature is available in Postfix 2.2 and later. 


