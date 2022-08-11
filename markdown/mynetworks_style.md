# mynetworks_style (default: Postfix ≥ 3.0: host, Postfix < 3.0: subnet)

The method to generate the default value for the mynetworks parameter.
This is the list of trusted networks for relay access control etc.



* Specify "mynetworks\_style = host" when Postfix should
"trust" only the local machine.
* Specify "mynetworks\_style = subnet" when Postfix
should "trust" remote SMTP clients in the same IP subnetworks as the local
machine. On Linux, this works correctly only with interfaces
specified with the "ifconfig" or "ip" command.
* Specify "mynetworks\_style = class" when Postfix should
"trust" remote SMTP clients in the same IP class A/B/C networks as the
local machine. Caution: this may cause
Postfix to "trust" your entire provider's network. Instead, specify
an explicit mynetworks list by hand, as described with the mynetworks
configuration parameter.


