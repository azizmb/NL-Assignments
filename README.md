NextLeap Programming Assignment
===============================

Problem 1
---------

Write a function which returns tuples of length ‘l’, each of which is a sub-sequence
of all elements in input pool.
Expected output :
- The output should be in lexicographical sort ordered tuples.
- Consider all the elements uniqueness based on their position not by
their value
- The factor l (the length of each return result tuple) should always be in
return tuple results when 0 <= l <= n or zero when r > n.
Example :


    input →
        F(“WXYZ”, 2)
    Output →
        ('W', 'X');
        ('W', 'Y');
        ('W', 'Z');
        ('X', 'Y');
        ('X', 'Z');
        ('Y', 'Z');
    
    
    input →
        F(“WWYZ”, 3)
    Output →
        ('W', 'W', 'Y');
        ('W', 'W', 'Z');
        ('W', 'Y', 'Z');
        ('W', 'Y', 'Z');
    
    
    input →
        F(“WXYZ”, 5)
    Output →
        None


Problem 2
---------

Write a function which takes a string as it’s input and returns a URL encoded format
of the same. Well its obvious that you can't use an inbuilt function.
Reference : http://www.w3schools.com/TAGS/ref_urlencode.asp
http://www.blooberry.com/indexdot/html/topics/urlencoding.htm
Expected output :
- Take a string URL input and produce output as a form of URL encoded
string.
- Consider w3 rules of url size and length of parameters


Example :

    input
        (“http://abcdef.com/whatever/something?a=ahem&b=1234&c=ok-thats-it#params{'from':'here'}”)
    Output
        “http%3A%2F%2Fabcdef.com%2Fwhatever%2Fsomething%3Fa%3Dahem%26b%3D1234%26c%3Dok-thats-it%23params%7B'from'%3A'here'%7D”


P.S. If you are done with the above problem then, I think its easy to make a
reverse of it, Say URL Decoder. WAF to URL decode the encoded input.


Problem 3
---------

Design and implement a simple QnA forum using Django. Assume that the system
is publicly accessible and does not require a user to register and log in. One can
directly post the question and can answer them. Just like stack-overflow or yahoo
answers. The flow and the spec of the application is as follows :
1. Application shall consist of two types of pages only.
    a. Landing page
    b. Individual question page
2. Landing page
    a. This shall have a prominent question field on top alongside an ‘Ask’ 
button. One can ask random questions and post them right away.
A ‘Post As’ field can also be included to incorporate name information
with that question, just for the sake of identifying who posted it.
    b. Landing page shall also list recent activity of questions being answered
and the answers being posted. Question and answer links shall be
clickable and would land on Individual Question Page explained in
3. This may be implemented via an RSS feed which gets updated as
per it’s TTL value. Front-end updates the feed over AJAX i.e. without
loading the page. (Similar to what Twitter does).
    c. Ref. http://www.jjude.com/2008/06/adding-rss-feeds-to-django-
applications/
3. Individual question page
    a. This page shall display the question in bold and on top of the page
    b. Question shall be followed by the answers posted
    c. Finally, there shall be an empty field which may allow a user to post an
answer
    d. Answers may be rated up and down (Stackoverflow-like) and shall be
displayed in the sorted order of their rating, best answer shown first.


Great To Have :
- A pagination of questions and answers in case loading all of them is ruining
it.
- One click standard RSS feed that can be subscribed with standard RSS
readers and email clients. You can make use of libraries.
- Brownie points for a good UI

