# export_environment (default: see "postconf -d" output)

The list of environment variables that a Postfix process will export
to non-Postfix processes. The TZ variable is needed for sane
time keeping on System-V-ish systems.




Specify a list of names and/or name=value pairs, separated by
whitespace or comma. Specify "{ name=value }" to protect whitespace
or comma in parameter values (whitespace after the opening "{" and
before the closing "}"
is ignored). The form name=value is supported with Postfix version
2.1 and later; the use of {} is supported with Postfix 3.0 and
later. 



Example:




```

export\_environment = TZ PATH=/bin:/usr/bin

```

