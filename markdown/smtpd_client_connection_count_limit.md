# smtpd_client_connection_count_limit (default: 50)

How many simultaneous connections any client is allowed to
make to this service. By default, the limit is set to half
the default process limit value.




To disable this feature, specify a limit of 0.




WARNING: The purpose of this feature is to limit abuse. It must
not be used to regulate legitimate mail traffic.




This feature is available in Postfix 2.2 and later.



