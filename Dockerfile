FROM python:3.7-alpine
MAINTAINER Christopher De Vries <devries@idolstarastronomer.com>

RUN apk add --update \
    gcc \
    make \
    musl-dev \
    libuv-dev \
    libxml2-dev \
    libxslt-dev \
  && rm -rf /var/cache/apk/*

RUN python -m pip install sanic lxml jinja2

RUN addgroup -g 2000 apprunner
RUN adduser -u 2000 -G apprunner -S apprunner

COPY main_app.py /app/
COPY static /app/static
WORKDIR /app
RUN chown -R apprunner:apprunner /app

ENV PORT 8080
EXPOSE 8080

USER apprunner

CMD python -m sanic main_app.app --host 0.0.0.0 --port $PORT --workers 4
