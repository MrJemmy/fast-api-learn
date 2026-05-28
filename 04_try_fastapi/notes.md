- pyenv shell <version>, pyenv shell --unset
- pyenv local <version>, for particular project folder
- pyenv global <version>, pyenv global system

### fast api installation 
- fastapi==0.118.0
- uvicorn==0.37.0 // for server
- gunicorn==23.0.0  // for server
- sqlmodel==0.0.25 = pydantic + sqlalchemy // ORM
- timescaledb ? his custom ORM


### to run fastapi
- uvicorn main:app --reload

### setup docker file for python fast api  
-  [blog for fast api docker file](https://codingforentrepreneurs.com/blog/deploy-fastapi-to-railway-with-this-dockerfile)


### build docker file
- `docker build -t project-name:v1 -f DockerFile.web .`
- `-t` project run or container name which we want, also we can specify `version` also
- `-f` Docker file name 
- `.` in currun directory 
- `docker run project-name`


### run compose file
- `docker compose up --watch`
- `docker compose down`  or `docker compose down -v` (to remove volumes)
- `docker compose run app /bin/bash` or `docker compose run app python`
- `app /bin/bash` : to acces bash(command line) of app which is name which we given to service
- `app python`: to directly access the python terminal 

### down compose down
- `docker compose down -v`
- this will remove the volumes, so it will remove database stuf also 

### what this command dose?
- `docker compose up --build --detach`