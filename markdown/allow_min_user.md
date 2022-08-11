# allow_min_user (default: no)

Allow a sender or recipient address to have `-' as the first
character. By
default, this is not allowed, to avoid accidents with software that
passes email addresses via the command line. Such software
would not be able to distinguish a malicious address from a
bona fide command-line option. Although this can be prevented by
inserting a "--" option terminator into the command line, this is
difficult to enforce consistently and globally. 


 As of Postfix version 2.5, this feature is implemented by
trivial-rewrite(8). With earlier versions this feature was implemented
by qmgr(8) and was limited to recipient addresses only. 


