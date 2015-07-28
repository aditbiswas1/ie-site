IE  Nitk  Website
==========

This is the repository for development of the institution of engineers NITK chapter website.
The project is primarily writted in python using the django framework.

Installation
------------
1. install python 2
2. install virtualenv, follow the steps given at [virtualenv]
3. clone this project using git clone
    ```sh
    git clone [git-repo-url]
    cd ie-site
    ```
4. create a virtualenv with any name  and activate it  
   
    ```sh
    virtualenv env
    source env/bin/activate
    
    ```
5. install the dependencies in the project directory
        
    ```sh
    sudo apt-get install python-dev libjpeg-dev libfreetype6-dev zlib1g-dev
    pip install PIL --allow-external PIL --allow-unverified PIL   
    pip install -r requirements.txt
    
    ```

6. run database sync and migrations
    ```sh
    python manage.py syncdb
    python manage.py migrate
    ```

7. start the django server
    
    ```sh
    python manage.py runserver
    ```

version
----
0.0.1

[virtualenv]: http://virtualenv.readthedocs.org/en/latest/virtualenv.html
