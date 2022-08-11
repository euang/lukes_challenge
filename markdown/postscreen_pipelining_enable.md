# postscreen_pipelining_enable (default: no)
 Enable "pipelining" SMTP protocol tests in the postscreen(8)
server. These tests are expensive: a good client must disconnect
after it passes the test, before it can talk to a real Postfix SMTP
server. 


 This feature is available in Postfix 2.8. 


