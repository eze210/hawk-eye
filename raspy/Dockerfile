FROM fedora

RUN dnf -y update
RUN dnf -y install python
RUN dnf -y install net-tools
RUN dnf -y install opencv
RUN dnf -y install python-opencv

WORKDIR /raspy

EXPOSE 8000
