# enable_long_queue_ids (default: no)
 Enable long, non-repeating, queue IDs (queue file names). The
benefit of non-repeating names is simpler logfile analysis and
easier queue migration (there is no need to run "postsuper" to
change queue file names that don't match their message file inode
number). 


 Note: see below for how to convert long queue file names to
Postfix ≤ 2.8. 


 Changing the parameter value to "yes" has the following effects:



* Existing queue file names are not affected.
* New queue files are created with names such as 3Pt2mN2VXxznjll.
These are encoded in a 52-character alphabet that contains digits
(0-9), upper-case letters (B-Z) and lower-case letters (b-z). For
safety reasons the vowels (AEIOUaeiou) are excluded from the alphabet.
The name format is: 6 or more characters for the time in seconds,
4 characters for the time in microseconds, the 'z'; the remainder
is the file inode number encoded in the first 51 characters of the
52-character alphabet.
* New messages have a Message-ID header with
*queueID*@*myhostname*.
* The mailq (postqueue -p) output has a wider Queue ID column.
The number of whitespace-separated fields is not changed.
* The hash\_queue\_depth algorithm uses the first characters
of the queue file creation time in microseconds, after conversion
into hexadecimal representation. This produces the same queue hashing
behavior as if the queue file name was created with "enable\_long\_queue\_ids
= no".


 Changing the parameter value to "no" has the following effects:



* Existing long queue file names are renamed to the short
form (while running "postfix reload" or "postsuper").
* New queue files are created with names such as C3CD21F3E90
from a hexadecimal alphabet that contains digits (0-9) and upper-case
letters (A-F). The name format is: 5 characters for the time in
microseconds; the remainder is the file inode number.
* New messages have a Message-ID header with
*YYYYMMDDHHMMSS.queueid*@*myhostname*, where
*YYYYMMDDHHMMSS* are the year, month, day, hour, minute and
second.
* The mailq (postqueue -p) output has the same format as
with Postfix ≤ 2.8.
* The hash\_queue\_depth algorithm uses the first characters
of the queue file name, with the hexadecimal representation of the
file creation time in microseconds.


 Before migration to Postfix ≤ 2.8, the following commands
are required to convert long queue file names into short names: 



```

# postfix stop
# postconf enable\_long\_queue\_ids=no
# postsuper

```

 Repeat the postsuper command until it reports no more queue file
name changes. 


 This feature is available in Postfix 2.9 and later. 


