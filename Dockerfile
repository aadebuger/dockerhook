FROM dockerfile/python
RUN apt-get update
RUN apt-get install -y python-setuptools
RUN easy_install docker-py
ADD ./src/main/python /myworkspace
WORKINGDIR /myworkspace
CMD ["python", "dockercloud/containerevent.py"]
