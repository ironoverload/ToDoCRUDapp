FROM ubuntu:latest
LABEL authors="steph"

ENTRYPOINT ["top", "-b"]