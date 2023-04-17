It is a Blogging Api designed with django rest framework

---------------------Important URLS------------------------------

register -> http://127.0.0.1:8000/auth/register/

login -> http://127.0.0.1:8000/auth/login/

blogs -> http://127.0.0.1:8000/blogs/

comments -> http://127.0.0.1:8000/blogs/comments/<blog_id>

reply -> http://127.0.0.1:8000/blogs/comments/reply/<comment_id>

-----------------------------------------------------------------

For register call the api http://127.0.0.1:8000/auth/register/ with post request and provide username and password
to genrate a new token which will be further used for authentication purpose for visiting the blogs

For login call the api http://127.0.0.1:8000/auth/login/ with post request and provide username and password
which will furthur genrate a token which will be used for authentication purpose for visiting the blogs


From here on Pass the new token along with the urls for proper authentication

For fetching all the blogs call the api http://127.0.0.1:8000/blogs/ with get request

For fetching specific blogs to perform curd operation call the api http://127.0.0.1:8000/blogs/<blog_id> with post request
user will only be able to update the likes and can't perform curd operation on blogs if the blog was not written by him.

For fetching all the comments of a specific blog call the api http://127.0.0.1:8000/blogs/comments/<blog_id>/ with 
specific get or post request by fetching and adding new comments respectively.

For fetching all the replys of a specific comment call the api http://127.0.0.1:8000/blogs/comments/reply/<comment_id>/ with 
specific get or post request by fetching and adding new reply on a comment respectively.
