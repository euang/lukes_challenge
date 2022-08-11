# local_command_shell (default: empty)

Optional shell program for local(8) delivery to non-Postfix commands.
By default, non-Postfix commands are executed directly; commands
are given to the default shell (typically, /bin/sh) only when they
contain shell meta characters or shell built-in commands.



 "sendmail's restricted shell" (smrsh) is what most people will
use in order to restrict what programs can be run from e.g. .forward
files (smrsh is part of the Sendmail distribution). 


 Note: when a shell program is specified, it is invoked even
when the command contains no shell built-in commands or meta
characters. 



Example:




```

local\_command\_shell = /some/where/smrsh -c
local\_command\_shell = /bin/bash -c

```

