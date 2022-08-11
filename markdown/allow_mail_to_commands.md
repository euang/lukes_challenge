# allow_mail_to_commands (default: alias, forward)

Restrict local(8) mail delivery to external commands. The default
is to disallow delivery to "|command" in :include: files (see
aliases(5) for the text that defines this terminology).




Specify zero or more of: **alias**, **forward** or **include**,
in order to allow commands in aliases(5), .forward files or in
:include: files, respectively.




Example:




```

allow\_mail\_to\_commands = alias,forward,include

```

