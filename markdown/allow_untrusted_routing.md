# allow_untrusted_routing (default: no)

Forward mail with sender-specified routing (user[@%!]remote[@%!]site)
from untrusted clients to destinations matching $relay\_domains.




By default, this feature is turned off. This closes a nasty open
relay loophole where a backup MX host can be tricked into forwarding
junk mail to a primary MX host which then spams it out to the world.




This parameter also controls if non-local addresses with sender-specified
routing can match Postfix access tables. By default, such addresses
cannot match Postfix access tables, because the address is ambiguous.



