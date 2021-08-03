FROM alpine:edge
EXPOSE 8000
WORKDIR /home

# TODO: 2-stage build

RUN apk add python3 python3-dev py3-pip musl-dev gcc g++ git build-base
RUN pip3 install gunicorn uvicorn

COPY envs/prod/alpine-packages.txt /tmp/
RUN cat /tmp/alpine-packages.txt | xargs apk add

COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY src ./
# TODO: avoid copying .env to container
# COPY .env ./

CMD ["entrypoint.sh"]
