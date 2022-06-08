# pyanalizer
To the project work, it's necessery follow libs:

    1. Redis ( database cache )
    2. Celery ( Queue worker admnistrator )
    3. Pickle ( Front end library )
    
## Instalation:

    - Installing [redis](https://phoenixnap.com/kb/install-redis-on-ubuntu-20-04):
    
        ```
        sudo apt install redis-server
        pip install redis
        ```
        
    - Installing [celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html#installation):
    
        ```
        pip install -U Celery
        ```
        
## Using:

    1. Clone this project
    2. Execute ```celery -A celery_queues worker -l info -c 10``` in the same folder for main.py
    3. Execute ```python3 main.py```
    4. Be happy
