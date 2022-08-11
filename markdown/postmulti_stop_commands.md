# postmulti_stop_commands (default: see "postconf -d" output)
 The postfix(1) commands that the postmulti(1) instance manager treats
as "stop" commands. For these commands, disabled instances are skipped,
and enabled instances are processed in reverse order. 


 This feature is available in Postfix 2.6 and later. 


