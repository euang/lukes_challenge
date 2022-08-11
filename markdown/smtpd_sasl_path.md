# smtpd_sasl_path (default: smtpd)
 Implementation-specific information that the Postfix SMTP server
passes through to
the SASL plug-in implementation that is selected with
**smtpd\_sasl\_type**. Typically this specifies the name of a
configuration file or rendezvous point. 


 This feature is available in Postfix 2.3 and later. In earlier
releases it was called **smtpd\_sasl\_application\_name**. 


