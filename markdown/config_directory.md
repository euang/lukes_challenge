# config_directory (default: see "postconf -d" output)
 The default location of the Postfix main.cf and master.cf
configuration files. This can be overruled via the following
mechanisms: 


* The MAIL\_CONFIG environment variable (daemon processes
and commands).
* The "-c" command-line option (commands only).


 With Postfix commands that run with set-gid privileges, a
config\_directory override either requires root privileges, or it
requires that the directory is listed with the alternate\_config\_directories
parameter in the default main.cf file. 


