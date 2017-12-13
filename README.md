# Team10Project

A fully distributed web crawler. 

# Features
* Highly scalable
* Control crawl rate by varying producer or consumer nodes
* Fault tolerant
* Easy deployment through docker

# Components and Libraries
* AWS EC2
* Kafka
* Zookeeper
* MongoDB
* Docker
* urllib
* BeautifulSoup

# Setup
* Start Zookeeper, Kafka and MongoDB instances in different nodes
* Put the the IP addresses in config.cfg
* Start the config server in a separate node by running config.py
* Dockerize producer and consumer using the script provided
* Start multiple producers and consumers using the docker image and AWS ECR
* Check the WikiGraph collection in MongoDB for results

# Analytics - Count the number of webpages referencing a particular node
* Map function
```
var mapFunction = function() {
    for(var i = 0; i < this.children.length;i++) {
        emit(this.children[i], 1);
    }
}
```
* Reduce functuon
```
var reduceFunction = function(key, obj) {
   return Array.sum(obj);
}
```
* Run mapreduce
```
db.WikiGraph.mapReduce(mapFunction, reduceFunction, { out : "total"});
```
* Check output
```
db.total.find().sort({value:-1}).limit(5).pretty()
```
# Read more about our project
* [Presentation](https://docs.google.com/presentation/d/11xJGloeuTd8Q0f_yiLlnOZLgsi8kChl0_I2fWaJETfA/edit?usp=sharing)
* [Paper](https://drive.google.com/file/d/1PNAtPh9JGf7-zx6H2-nNzlSrGAmqOwBy/view?usp=sharing)
