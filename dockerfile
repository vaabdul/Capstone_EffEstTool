FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5555
CMD python ./app.py

#Docker commands
#docker build -t my-python:0.0.1.RELEASE .
#docker container run -d -p 5500:5500 my-python:0.0.1.RELEASE 
#docker run -p 8081:8080 my-python:0.0.1.RELEASE
#docker container run -d -p 5500:5500 my-python:0.0.1.RELEASE
#9e0218651eca54e79a4526bee20864eb605fc00920fc917831832bd776591b4d
