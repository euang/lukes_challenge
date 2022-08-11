# message_size_limit (default: 10240000)

The maximal size in bytes of a message, including envelope information.
The value cannot exceed LONG\_MAX (typically, a 32-bit or 64-bit
signed integer).



 Note: be careful when making changes. Excessively small values
will result in the loss of non-delivery notifications, when a bounce
message size exceeds the local or remote MTA's message size limit.



