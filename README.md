# CFlix - Internal Streaming Service App

## Stay tuned for further Developments

### Steps to deploy on to your server

- Create a .env file in the root directory of the project
- Add the following options according to your need
    - SECRET_KEY
    - DB_NAME
    - DB_USER
    - DB_PASSWD
    - DB_HOST
    - DB_PORT
- PostgreSQL is a essential system requirement, please install before using this app
- Add your domain name / IP Address in the ALLOWED_HOSTS list in the settings.py file
- Usage of SSL: Either setup your own certificate or get one from a provider
- Disable SSL: Comment Out Every thing (that is add a '#' before revery statement in the Security section of settings.py)