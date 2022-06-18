# pyanalizer
To the project work, it's necessery follow libs:

    1. Redis ( database cache )
    2. Celery ( Queue worker admnistrator )
    3. Matplotlib ( Front end library )
    4. Tkinter ( Front end library )
    5. Pandas ( Front end library )
    
    
## Instalation:

    - Installing [redis](https://phoenixnap.com/kb/install-redis-on-ubuntu-20-04):
    
    - Installing [celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html#installation):
    
    - Installing [Matlotlib](https://matplotlib.org/stable/users/installing/index.html)
    
    - Installing [Tkinter](https://stackoverflow.com/questions/26702119/installing-tkinter-on-ubuntu-14-04)
    
    - Installing [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
        
## Using:

    1. Clone this project
    2. Execute in your terminal ```redis-server```
    2. Execute in other prompt ```celery -A celery_queues worker -l info -c 10``` in the same folder for main.py
    3. Execute ```python3 main.py```
    4. Be happy
