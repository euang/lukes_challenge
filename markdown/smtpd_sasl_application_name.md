# smtpd_sasl_application_name (default: smtpd)

The application name that the Postfix SMTP server uses for SASL
server initialization. This
controls the name of the SASL configuration file. The default value
is **smtpd**, corresponding to a SASL configuration file named
**smtpd.conf**.




This feature is available in Postfix 2.1 and 2.2. With Postfix 2.3
it was renamed to smtpd\_sasl\_path.



