FROM python:3.8

# Install dependencies
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Include the app code
COPY ./app /app
WORKDIR /app

#Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]