# Contact form microservice

## Environment variables
* **stmp_server** The SMTP server to use (e.g. `smtp.gmail.com`)
* **smtp_port** The SMTP port (Optional; Defaults to SMTP SSL port 465)
* **email_from** The email address and username on the server (e.g. `support@example.org`)
* **email_pwd** The corresponding password
* **email_to** The email address of the recipient. (Optional; By default this is the same as the sender)

## Gmail
To use a Gmail account for sending the emails, enable "Allow less secure apps" [here](https://myaccount.google.com/u/1/lesssecureapps).

## Run locally
1. Install requirements with `pip3 install -r requirements.txt`
2. Add .env file to root of project directory
3. Run app with `uvicorn --env-file ./.env --app-dir ./app/ main:app`
4. Explore API at http://127.0.0.1:8000

## Deployment
The application can be run inside a docker container with  
`docker build -t contactform .`  
`docker run -d --env-file ./.env --name contactform -p 80:80 contactform`
