# mailbox_transport_maps (default: empty)
 Optional lookup tables with per-recipient message delivery
transports to use for local(8) mailbox delivery, whether or not the
recipients are found in the UNIX passwd database. 


 The precedence of local(8) delivery features from high to low
is: aliases, .forward files, mailbox\_transport\_maps, mailbox\_transport,
mailbox\_command\_maps, mailbox\_command, home\_mailbox, mail\_spool\_directory,
fallback\_transport\_maps, fallback\_transport and luser\_relay. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 For safety reasons, this feature does not allow $number
substitutions in regular expression maps. 


 This feature is available in Postfix 2.3 and later. 


