# alpine python
FROM alpine:3.8

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# flask app
COPY ./ /app/

WORKDIR /app

RUN find -name "*.pyc" -delete && \
    pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
