# hash_queue_depth (default: 1)

The number of subdirectory levels for queue directories listed with
the hash\_queue\_names parameter. Queue hashing is implemented by
creating one or more levels of directories with one-character names.
Originally, these directory names were equal to the first characters
of the queue file name, with the hexadecimal representation of the
file creation time in microseconds. 


 With long queue file names, queue hashing produces the same
results as with short names. The file creation time in microseconds
is converted into hexadecimal form before the result is used for
queue hashing. The base 16 encoding gives finer control over the
number of subdirectories than is possible with the base 52 encoding
of long queue file names. 



After changing the hash\_queue\_names or hash\_queue\_depth parameter,
execute the command "**postfix reload**".



