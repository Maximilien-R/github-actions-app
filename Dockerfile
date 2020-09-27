FROM python:3.8.6

RUN apt-get update && apt-get install -y cmake bison flex \
      && mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app/

ARG requirement_file="production.txt"
COPY requirements/. /usr/src/app/requirements
RUN pip install --no-cache-dir -r requirements/$requirement_file

COPY . /usr/src/app

EXPOSE 80

RUN chmod +x .docker/docker-entrypoint.sh

ENTRYPOINT [ "/usr/src/app/.docker/docker-entrypoint.sh" ]

CMD [ "python", "-m", "github_actions_app" ]
