# compatibility_level (default: 0)
 A safety net that causes Postfix to run with backwards-compatible
default settings after an upgrade to a newer Postfix version. 


 With backwards compatibility turned on (the main.cf compatibility\_level
value is less than the Postfix built-in value), Postfix looks for
settings that are left at their implicit default value, and logs a
message when a backwards-compatible default setting is required.




> 
> 
> ```
> 
> using backwards-compatible default setting *name=value*
>     to [accept a specific client request]
> 
> using backwards-compatible default setting *name=value*
>     to [enable specific Postfix behavior]
> 
> ```
> 
> 


 See COMPATIBILITY\_README for specific message details. If such
a message is logged in the context of a legitimate request, the
system administrator should make the backwards-compatible setting
permanent in main.cf or master.cf, for example: 



> 
> 
> ```
> 
> # **postconf** *name=value*
> # **postfix reload**
> 
> ```
> 
> 


 When no more backwards-compatible settings need to be made
permanent, the administrator should turn off backwards compatibility
by updating the compatibility\_level setting in main.cf:



> 
> 
> ```
> 
> # **postconf compatibility\_level=*N***
> # **postfix reload**
> 
> ```
> 
> 


 For *N* specify the number that is logged in your postfix(1)
warning message: 



> 
> 
> ```
> 
> warning: To disable backwards compatibility use "postconf
>     compatibility\_level=*N*" and "postfix reload"
> 
> ```
> 
> 


 Starting with Postfix version 3.6, the compatibility level in
the above warning message is the Postfix version that introduced
the last incompatible change. The level is formatted as
*major.minor.patch*, where *patch* is usually omitted and
defaults to zero. Earlier compatibility levels are 0, 1 and 2. 


 NOTE: this also introduces support for the "<level",
"<=level", and other operators to compare compatibility levels.
With the standard operators "<", "<=", etc., compatibility
level "3.10" would be smaller than "3.9" which is undesirable. 


 This feature is available in Postfix 3.0 and later. 


