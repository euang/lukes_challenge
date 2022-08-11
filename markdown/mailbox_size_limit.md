# mailbox_size_limit (default: 51200000)
 The maximal size of any local(8) individual mailbox or maildir
file, or zero (no limit). In fact, this limits the size of any
file that is written to upon local delivery, including files written
by external commands that are executed by the local(8) delivery
agent. The value cannot exceed LONG\_MAX (typically, a 32-bit or
64-bit signed integer).




This limit must not be smaller than the message size limit.



