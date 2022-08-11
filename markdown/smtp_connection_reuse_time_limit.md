# smtp_connection_reuse_time_limit (default: 300s)
 The amount of time during which Postfix will use an SMTP
connection repeatedly. The timer starts when the connection is
initiated (i.e. it includes the connect, greeting and helo latency,
in addition to the latencies of subsequent mail delivery transactions).



 This feature addresses a performance stability problem with
remote SMTP servers. This problem is not specific to Postfix: it
can happen when any MTA sends large amounts of SMTP email to a site
that has multiple MX hosts. 


 The problem starts when one of a set of MX hosts becomes slower
than the rest. Even though SMTP clients connect to fast and slow
MX hosts with equal probability, the slow MX host ends up with more
simultaneous inbound connections than the faster MX hosts, because
the slow MX host needs more time to serve each client request. 


 The slow MX host becomes a connection attractor. If one MX
host becomes N times slower than the rest, it dominates mail delivery
latency unless there are more than N fast MX hosts to counter the
effect. And if the number of MX hosts is smaller than N, the mail
delivery latency becomes effectively that of the slowest MX host
divided by the total number of MX hosts. 


 The solution uses connection caching in a way that differs from
Postfix version 2.2. By limiting the amount of time during which a connection
can be used repeatedly (instead of limiting the number of deliveries
over that connection), Postfix not only restores fairness in the
distribution of simultaneous connections across a set of MX hosts,
it also favors deliveries over connections that perform well, which
is exactly what we want. 


 The default reuse time limit, 300s, is comparable to the various
smtp transaction timeouts which are fair estimates of maximum excess
latency for a slow delivery. Note that hosts may accept thousands
of messages over a single connection within the default connection
reuse time limit. This number is much larger than the default Postfix
version 2.2 limit of 10 messages per cached connection. It may prove necessary
to lower the limit to avoid interoperability issues with MTAs that
exhibit bugs when many messages are delivered via a single connection.
A lower reuse time limit risks losing the benefit of connection
reuse when the average connection and mail delivery latency exceeds
the reuse time limit. 


 This feature is available in Postfix 2.3 and later. 


