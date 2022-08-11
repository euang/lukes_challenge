# remote_header_rewrite_domain (default: empty)
 Don't rewrite message headers from remote clients at all when
this parameter is empty; otherwise, rewrite message headers and
append the specified domain name to incomplete addresses. The
local\_header\_rewrite\_clients parameter controls what clients Postfix
considers local. 


 Examples: 


 The safe setting: append "domain.invalid" to incomplete header
addresses from remote SMTP clients, so that those addresses cannot
be confused with local addresses. 



> 
> 
> ```
> 
> remote\_header\_rewrite\_domain = domain.invalid
> 
> ```
> 
> 


 The default, purist, setting: don't rewrite headers from remote
clients at all. 



> 
> 
> ```
> 
> remote\_header\_rewrite\_domain =
> 
> ```
> 
> 


