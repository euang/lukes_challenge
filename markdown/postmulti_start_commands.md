# postmulti_start_commands (default: start)
 The postfix(1) commands that the postmulti(1) instance manager treats
as "start" commands. For these commands, disabled instances are "checked"
rather than "started", and failure to "start" a member instance of an
instance group will abort the start-up of later instances. 


 This feature is available in Postfix 2.6 and later. 


