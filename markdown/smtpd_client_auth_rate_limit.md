# smtpd_client_auth_rate_limit (default: 0)

The maximal number of AUTH commands that any client is allowed to
send to this service per time unit, regardless of whether or not
Postfix actually accepts those commands. The time unit is specified
with the anvil\_rate\_time\_unit configuration parameter.




By default, there is no limit on the number of AUTH commands that a
client may send.




To disable this feature, specify a limit of 0.




WARNING: The purpose of this feature is to limit abuse. It must
not be used to regulate legitimate mail traffic.




This feature is available in Postfix 3.1 and later.



