FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    apt-get clean

WORKDIR /webapp
RUN python3 -m venv venv
ENV PATH="/webapp/venv/bin:$PATH"
COPY . /webapp
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
