FROM ubuntu:16.04

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y wget software-properties-common python-software-properties python-setuptools python-dev build-essential
RUN wget -qO - http://packages.confluent.io/deb/3.3/archive.key | apt-key add -
RUN add-apt-repository "deb [arch=amd64] http://packages.confluent.io/deb/3.3 stable main"
RUN apt-get update && apt-get install -y librdkafka-dev python-pip
RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .
ENTRYPOINT ["python", "UrlConsumer.py"]
CMD [ "python", "./UrlConsumer.py" ]