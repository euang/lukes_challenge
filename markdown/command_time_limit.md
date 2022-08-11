# command_time_limit (default: 1000s)

Time limit for delivery to external commands. This limit is used
by the local(8) delivery agent, and is the default time limit for
delivery by the pipe(8) delivery agent.




Note: if you set this time limit to a large value you must update the
global ipc\_timeout parameter as well.



