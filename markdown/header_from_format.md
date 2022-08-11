# header_from_format (default: standard)
 The format of the Postfix-generated **From:** header. This
setting affects the appearance of 'full name' information when a
local program such as /bin/mail submits a message without a From:
header through the Postfix sendmail(1) command. 


 Specify one of the following: 



**standard** (default)  Produce a header formatted
as "**From:** *name* **<***address***>**".
This is the default as of Postfix 3.3.
**obsolete** Produce a header formatted as "**From:**
*address* **(***name***)**". This is the behavior
prior to Postfix 3.3. 

 Notes: 


* Postfix generates the format "**From:** *address*"
when *name* information is unavailable or the envelope sender
address is empty. This is the same behavior as prior to Postfix
3.3.
* In the **standard** form, the *name* will be quoted
if it contains **specials** as defined in RFC 5322, or the "!%"
address operators.
* The Postfix sendmail(1) command gets *name* information
from the **-F** command-line option, from the **NAME**
environment variable, or from the UNIX password file.


 This feature is available in Postfix 3.3 and later. 


