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
![Landing Page](http://i.imgur.com/gDhc4.png)
![Question Page](http://i.imgur.com/2sKaJ.png)    
    