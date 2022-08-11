# tls_wildcard_matches_multiple_labels (default: yes)
 Match multiple DNS labels with "\*" in wildcard certificates.



 Some mail service providers prepend the customer domain name
to a base domain for which they have a wildcard TLS certificate.
For example, the MX records for example.com hosted by example.net
may be: 



> 
> 
> ```
> 
> example.com. IN MX 0 example.com.mx1.example.net.
> example.com. IN MX 0 example.com.mx2.example.net.
> 
> ```
> 
> 


 and the TLS certificate may be for "\*.example.net". The "\*"
then corresponds with multiple labels in the mail server domain
name. While multi-label wildcards are not widely supported, and
are not blessed by any standard, there is little to be gained by
disallowing their use in this context. 


 Notes: 




* In a certificate name, the "\*" is special only when it is
used as the first label.
* While Postfix (2.11 or later) can match "\*" with multiple
domain name labels, other implementations likely will not.
* Earlier Postfix implementations behave as if
"tls\_wildcard\_matches\_multiple\_labels = no".


 This feature is available in Postfix 2.11 and later. 


