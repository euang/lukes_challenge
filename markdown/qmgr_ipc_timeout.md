# qmgr_ipc_timeout (default: 60s)
 The time limit for the queue manager to send or receive information
over an internal communication channel. The purpose is to break
out of deadlock situations. If the time limit is exceeded the
software either retries or aborts the operation. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.8 and later. 


