# alternate_config_directories (default: empty)

A list of non-default Postfix configuration directories that may
be specified with "-c config\_directory" on the command line (in the
case of sendmail(1), with the "-C" option), or via the MAIL\_CONFIG
environment parameter.




This list must be specified in the default Postfix main.cf file,
and will be used by set-gid Postfix commands such as postqueue(1)
and postdrop(1).




Specify absolute pathnames, separated by comma or space. Note: $name
expansion is not supported.



