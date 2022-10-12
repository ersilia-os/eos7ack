FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install bs4==4.11.1

WORKDIR /repo
COPY . /repo
