# unknown_local_recipient_reject_code (default: 550)

The numerical Postfix SMTP server response code when a recipient
address is local, and $local\_recipient\_maps specifies a list of
lookup tables that does not match the recipient. A recipient
address is local when its domain matches $mydestination,
$proxy\_interfaces or $inet\_interfaces.




The default setting is 550 (reject mail) but it is safer to initially
use 450 (try again later) so you have time to find out if your
local\_recipient\_maps settings are OK.




Example:




```

unknown\_local\_recipient\_reject\_code = 450

```


This feature is available in Postfix 2.0 and later.



