Instructions
============

Install dependencies:
-----------------

    cd problem3
    pip install -r requirements.txt


Create database tables:
-----------------------

    python manage.py syncdb --all
    python manage.py migrate --fake
    
    
Load test data (optional):
---------------

    python manage.py loaddata fixtures/test_data.json
    
    
Run development server:
-----------------------

    python manage.py runserver
    
The application can now be accessed by browsing to http://localhost:8000/


Screenshots:
------------
![screen1](http://i53.tinypic.com/2e16n0x.png)
![screen2](http://i55.tinypic.com/15o8d91.png)
![screen3](http://i52.tinypic.com/34zyrkp.png)
    
    