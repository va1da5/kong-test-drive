FROM python:3.9-alpine as build

WORKDIR /app

RUN apk add --update alpine-sdk

COPY requirements.txt .

RUN pip install -r requirements.txt


FROM python:3.9-alpine as release

WORKDIR /app

COPY --from=build /usr/local/lib/python3.9/ /usr/local/lib/python3.9/
COPY --from=build /usr/local/bin/ /usr/local/bin/

COPY main.py .

ENTRYPOINT [ "uvicorn" ]
CMD [ "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]