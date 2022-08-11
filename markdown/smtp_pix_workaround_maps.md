# smtp_pix_workaround_maps (default: empty)
 Lookup tables, indexed by the remote SMTP server address, with
per-destination workarounds for CISCO PIX firewall bugs. The table
is not indexed by hostname for consistency with
smtp\_discard\_ehlo\_keyword\_address\_maps. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 This feature is available in Postfix 2.4 and later. 


