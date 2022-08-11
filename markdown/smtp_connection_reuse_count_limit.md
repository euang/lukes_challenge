# smtp_connection_reuse_count_limit (default: 0)
 When SMTP connection caching is enabled, the number of times
that an SMTP session may be reused before it is closed, or zero (no
limit). With a reuse count limit of N, a connection is used up to
N+1 times. 


 NOTE: This feature is unsafe. When a high-volume destination
has multiple inbound MTAs, then the slowest inbound MTA will attract
the most connections to that destination. This limitation does not
exist with the smtp\_connection\_reuse\_time\_limit feature. 


 This feature is available in Postfix 2.11. 


