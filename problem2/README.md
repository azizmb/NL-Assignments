Instructions
============

To run unittests:
-----------------

    python test.py


To use function:
----------------

Encode:

    >>> import urlencode
    >>> url = "http://abcdef.com/whatever/something?a=ahem&b=1234&c=ok-thats-it#params{'from':'here'}"
    >>> print urlencode.encode(url)
    http%3A%2F%2Fabcdef.com%2Fwhatever%2Fsomething%3Fa%3Dahem%26b%3D1234%26c%3Dok-thats-it%23params%7B%27from%27%3A%27here%27%7D
    >>> 
    
Decode:

    >>> import urlencode
    >>> encoded_url = "http%3A%2F%2Fabcdef.com%2Fwhatever%2Fsomething%3Fa%3Dahem%26b%3D1234%26c%3Dok-thats-it%23params%7B%27from%27%3A%27here%27%7D"
    >>> print urlencode.dencode(url)
    http://abcdef.com/whatever/something?a=ahem&b=1234&c=ok-thats-it#params{'from':'here'}
    >>> 
    
    
