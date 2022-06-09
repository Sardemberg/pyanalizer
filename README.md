# pyanalizer
Instructions for running this project:
    - Install redis
    - Install python libs:
        - celery
        - redis
        - ploty

    - Execute this command in your terminal:
        - celery -A celery_queues worker -l info -c 10
        - In other command prompt, execute main file with python