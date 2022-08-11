# tcp_windowsize (default: 0)
 An optional workaround for routers that break TCP window scaling.
Specify a value > 0 and < 65536 to enable this feature. With
Postfix TCP servers (smtpd(8), qmqpd(8)), this feature is implemented
by the Postfix master(8) daemon. 


 To change this parameter without stopping Postfix, you need to
first terminate all Postfix TCP servers: 



> 
> 
> ```
> 
> # postconf -e master\_service\_disable=inet
> # postfix reload
> 
> ```
> 
> 


 This immediately terminates all processes that accept network
connections. Next, you enable Postfix TCP servers with the updated
tcp\_windowsize setting: 



> 
> 
> ```
> 
> # postconf -e tcp\_windowsize=65535 master\_service\_disable=
> # postfix reload
> 
> ```
> 
> 


 If you skip these steps with a running Postfix system, then the
tcp\_windowsize change will work only for Postfix TCP clients (smtp(8),
lmtp(8)). 


 This feature is available in Postfix 2.6 and later. 


