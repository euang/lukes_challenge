# lmtp_cache_connection (default: yes)

Keep Postfix LMTP client connections open for up to $max\_idle
seconds. When the LMTP client receives a request for the same
connection the connection is reused.



 This parameter is available in Postfix version 2.2 and earlier.
With Postfix version 2.3 and later, see lmtp\_connection\_cache\_on\_demand,
lmtp\_connection\_cache\_destinations, or lmtp\_connection\_reuse\_time\_limit.




The effectiveness of cached connections will be determined by the
number of remote LMTP servers in use, and the concurrency limit specified
for the Postfix LMTP client. Cached connections are closed under any of
the following conditions:



* The Postfix LMTP client idle time limit is reached. This limit is
specified with the Postfix max\_idle configuration parameter.
* A delivery request specifies a different destination than the
one currently cached.
* The per-process limit on the number of delivery requests is
reached. This limit is specified with the Postfix max\_use
configuration parameter.
* Upon the onset of another delivery request, the remote LMTP server
associated with the current session does not respond to the RSET
command.



Most of these limitations have been with the Postfix
connection cache that is shared among multiple LMTP client
programs.



