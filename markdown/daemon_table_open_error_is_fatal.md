# daemon_table_open_error_is_fatal (default: no)
 How a Postfix daemon process handles errors while opening lookup
tables: gradual degradation or immediate termination. 



  **no**  (default)    Gradual degradation: a
daemon process logs a message of type "error" and continues execution
with reduced functionality. Features that do not depend on the
unavailable table will work normally, while features that depend
on the table will result in a type "warning" message.   
 When
the notify\_classes parameter value contains the "data" class, the
Postfix SMTP server and client will report transcripts of sessions
with an error because a table is unavailable. 

 
  **yes**  (historical behavior)    Immediate
termination: a daemon process logs a type "fatal" message and
terminates immediately. This option reduces the number of possible
code paths through Postfix, and may therefore be slightly more
secure than the default. 

 

 For the sake of sanity, the number of type "error" messages is
limited to 13 over the lifetime of a daemon process. 


 This feature is available in Postfix 2.9 and later. 


