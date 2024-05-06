FROM ubuntu:23.10
RUN apt-get update -y && apt-get install -y python3-pip python-dev-is-python3
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY ./main /app/main/
COPY ./.env /app/.env
RUN apt install python3.11-venv -y && python -m venv new_env && /app/new_env/bin/pip install --upgrade pip
RUN /app/new_env/bin/pip install -r requirements.txt

CMD [ "/app/new_env/bin/python", "-m", "main.__init__"]
