# import_environment (default: see "postconf -d" output)
 The list of environment variables that a privileged Postfix
process will import from a non-Postfix parent process, or name=value
environment overrides. Unprivileged utilities will enforce the
name=value overrides, but otherwise will not change their process
environment. Examples of relevant environment variables: 



**TZ**
May be needed for sane time keeping on most System-V-ish systems.

**DISPLAY**
Needed for debugging Postfix daemons with an X-windows debugger. 
**XAUTHORITY**
Needed for debugging Postfix daemons with an X-windows debugger. 
**MAIL\_CONFIG**
Needed to make "**postfix -c**" work. 
**POSTLOG\_SERVICE**
Needed to make "**maillog\_file**" work during daemon
process initialization. 
**POSTLOG\_HOSTNAME**
Needed to make "**maillog\_file**" work during daemon
process initialization. 

 Specify a list of names and/or name=value pairs, separated by
whitespace or comma. Specify "{ name=value }" to protect whitespace
or comma in environment variable values (whitespace after the opening "{" and
before the closing "}"
is ignored). The form name=value is supported with Postfix version
2.1 and later; the use of {} is supported with Postfix 3.0 and
later. 


