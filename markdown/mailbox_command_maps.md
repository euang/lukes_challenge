# mailbox_command_maps (default: empty)

Optional lookup tables with per-recipient external commands to use
for local(8) mailbox delivery. Behavior is as with mailbox\_command.



 The precedence of local(8) delivery features from high to low
is: aliases, .forward files, mailbox\_transport\_maps, mailbox\_transport,
mailbox\_command\_maps, mailbox\_command, home\_mailbox, mail\_spool\_directory,
fallback\_transport\_maps, fallback\_transport and luser\_relay. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



