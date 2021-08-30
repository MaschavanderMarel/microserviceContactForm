# Contact form microservice

## Environment variables
* email_pwd = password for developer emailaccount @gmail.com

## Run locally
1. Install requirements with `pip3 install -r requirements.txt`
2. Add .env file to root of project directory
3. Run app with `uvicorn --env-file ./.env --app-dir ./app/ main:app`
4. Explore API at http://127.0.0.1:8000

## Deployment
The application can be run inside a docker container with  
`docker build -t contactform .`  
`docker run -d --env-file ./.env --name contactform -p 80:80 contactform`
