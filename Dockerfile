FROM python:3.9
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
expose 8000
CMD uvicorn main:app --host=0.0.0.0
