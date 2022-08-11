# multi_instance_wrapper (default: empty)
 The pathname of a multi-instance manager command that the
postfix(1) command invokes when the multi\_instance\_directories
parameter value is non-empty. The pathname may be followed by
initial command arguments separated by whitespace; shell
metacharacters such as quotes are not supported in this context.



 The postfix(1) command invokes the manager command with the
postfix(1) non-option command arguments on the manager command line,
and with all installation configuration parameters exported into
the manager command process environment. The manager command in
turn invokes the postfix(1) command for individual Postfix instances
as "postfix -c *config\_directory* *command*". 


 This feature is available in Postfix 2.6 and later. 


