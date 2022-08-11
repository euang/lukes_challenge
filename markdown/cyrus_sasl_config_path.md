# cyrus_sasl_config_path (default: empty)
 Search path for Cyrus SASL application configuration files,
currently used only to locate the $smtpd\_sasl\_path.conf file.
Specify zero or more directories separated by a colon character,
or an empty value to use Cyrus SASL's built-in search path. 


 This feature is available in Postfix 2.5 and later when compiled
with Cyrus SASL 2.1.22 or later. 


