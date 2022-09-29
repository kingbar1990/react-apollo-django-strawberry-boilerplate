FROM python:3.9

RUN pip install --upgrade pip



ADD ./pyproject.toml ./
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev
RUN poetry update

## -- Update system
#RUN apt-get update
#RUN apt-get install binutils libproj-dev gdal-bin -y

# -- Install Pipenv stable
#RUN pip install pipenv==v2018.10.9 --upgrade pip
#RUN pip install psycopg2
#
## Check system
#
## -- Install dependencies:
#ADD ./Pipfile ./tmp/Pipfile
#ADD ./Pipfile.lock ./tmp/Pipfile.lock
#RUN cd /tmp &&  pipenv install --system --deploy
#
## -- Update system
#RUN apt-get update
#RUN apt-get install binutils libproj-dev gdal-bin -y