# info_log_address_format (default: external)
 The email address form that will be used in non-debug logging
(info, warning, etc.). As of Postfix 3.5 when an address localpart
contains spaces or other special characters, the localpart will be
quoted, for example: 



> 
> 
> ```
> 
>     from=<"name with spaces"@example.com>
> 
> ```
> 
> 


 Older Postfix versions would log the internal (unquoted) form: 



> 
> 
> ```
> 
>     from=<name with spaces@example.com>
> 
> ```
> 
> 


 The external and internal forms are identical for the vast
majority of email addresses that contain no spaces or other special
characters in the localpart. 


 The logging in external form is consistent with the address
form that Postfix 3.2 and later prefer for most table lookups. This
is therefore the more useful form for non-debug logging. 


 Specify "**info\_log\_address\_format = internal**" for backwards
compatibility. 


 Postfix uses the unquoted form internally, because an attacker
can specify an email address in different forms by playing games
with quotes and backslashes. An attacker should not be able to use
such games to circumvent Postfix access policies. 


 This feature is available in Postfix 3.5 and later. 


