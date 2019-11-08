# DataEngineering-PubsubPublisher
This is a GCP cloud function, the event is trigger by a GCP bucket on object creation, and this code should publish a message for a topic previously created in Pup/Sub

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### 1- Prerequisites
* [Anaconda]() - Anaconda allows us to keep virtual environments organize and it is the best setup tool for data analysis. 

### 2- Setup

```sh
$ git clone ~/DataEngineering-PubsubPublisher.git
$ conda create -n PubsubPublisher python=3.7
$ conda activate PubsubPublisher
$ pip install requirements.txt
```

4.- For Windows - In order to create a Task Scheduler a bash is included here as well, change the path for the new directory as well as the name of the new environment and the executable bin path for conda.  
    For Unix - (This needs to be implemented)

## Authors
* **Enrique Plata ** - *2019/09/01*