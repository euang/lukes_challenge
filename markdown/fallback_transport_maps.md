# fallback_transport_maps (default: empty)
 Optional lookup tables with per-recipient message delivery
transports for recipients that the local(8) delivery agent could
not find in the aliases(5) or UNIX password database. 


 The precedence of local(8) delivery features from high to low
is: aliases, .forward files, mailbox\_transport\_maps, mailbox\_transport,
mailbox\_command\_maps, mailbox\_command, home\_mailbox, mail\_spool\_directory,
fallback\_transport\_maps, fallback\_transport and luser\_relay. 


 For safety reasons, this feature does not allow $number
substitutions in regular expression maps. 


 This feature is available in Postfix 2.3 and later. 


