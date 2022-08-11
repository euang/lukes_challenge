# virtual_minimum_uid (default: 100)

The minimum user ID value that the virtual(8) delivery agent accepts
as a result from $virtual\_uid\_maps table lookup. Returned
values less than this will be rejected, and the message will be
deferred.



 This parameter is specific to the virtual(8) delivery agent.
It does not apply when mail is delivered with a different mail
delivery program. 


