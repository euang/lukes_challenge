# postscreen_command_count_limit (default: 20)
 The limit on the total number of commands per SMTP session for
postscreen(8)'s built-in SMTP protocol engine. This SMTP engine
defers or rejects all attempts to deliver mail, therefore there is
no need to enforce separate limits on the number of junk commands
and error commands. 


 This feature is available in Postfix 2.8. 


