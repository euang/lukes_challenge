# debugger_command (default: empty)

The external command to execute when a Postfix daemon program is
invoked with the -D option.




Use "command .. & sleep 5" so that the debugger can attach before
the process marches on. If you use an X-based debugger, be sure to
set up your XAUTHORITY environment variable before starting Postfix.




Note: the command is subject to $name expansion, before it is
passed to the default command interpreter. Specify "$$" to
produce a single "$" character.




Example:




```

debugger\_command =
    PATH=/usr/bin:/usr/X11R6/bin
    ddd $daemon\_directory/$process\_name $process\_id & sleep 5

```

