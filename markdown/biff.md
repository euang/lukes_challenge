# biff (default: yes)

Whether or not to use the local biff service. This service sends
"new mail" notifications to users who have requested new mail
notification with the UNIX command "biff y".




For compatibility reasons this feature is on by default. On systems
with lots of interactive users, the biff service can be a performance
drain. Specify "biff = no" in main.cf to disable.



