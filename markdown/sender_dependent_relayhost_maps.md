# sender_dependent_relayhost_maps (default: empty)
 A sender-dependent override for the global relayhost parameter
setting. The tables are searched by the envelope sender address and
@domain. A lookup result of DUNNO terminates the search without
overriding the global relayhost parameter setting (Postfix 2.6 and
later). This information is overruled with relay\_transport,
sender\_dependent\_default\_transport\_maps, default\_transport and with
the transport(5) table. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 For safety reasons, this feature does not allow $number
substitutions in regular expression maps. 



This feature is available in Postfix 2.3 and later.



