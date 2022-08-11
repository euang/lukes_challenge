# enable_threaded_bounces (default: no)
 Enable non-delivery, success, and delay notifications that link
to the original message by including a References: and In-Reply-To:
header with the original Message-ID value. There are advantages and
disadvantages to consider. 



  **advantage**    This allows mail readers to present
a delivery status notification in the same email thread as the original
message. 
  **disadvantage**    This makes it easy for users to
mistakenly delete the whole email thread (all related messages),
instead of deleting only the non-delivery notification. 

 This feature is available in Postfix 3.6 and later. 


