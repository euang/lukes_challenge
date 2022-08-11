# local_destination_concurrency_limit (default: 2)
 The maximal number of parallel deliveries via the local mail
delivery transport to the same recipient (when
"local\_destination\_recipient\_limit = 1") or the maximal number of
parallel deliveries to the same local domain (when
"local\_destination\_recipient\_limit > 1"). This limit is enforced by
the queue manager. The message delivery transport name is the first
field in the entry in the master.cf file. 


 A low limit of 2 is recommended, just in case someone has an
expensive shell command in a .forward file or in an alias (e.g.,
a mailing list manager). You don't want to run lots of those at
the same time. 


