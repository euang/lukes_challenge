# fast_flush_refresh_time (default: 12h)

The time after which a non-empty but unread per-destination "fast
flush" logfile needs to be refreshed. The contents of a logfile
are refreshed by requesting delivery of all messages listed in the
logfile.




You can specify the time as a number, or as a number followed by
a letter that indicates the time unit: s=seconds, m=minutes, h=hours,
d=days, w=weeks. The default time unit is hours.



