FROM python:3.9

RUN apt-get install libjpeg-dev zlib1g-dev

# -- Upgrade pip
RUN pip install --upgrade pip

# -- Install Poetry stable
ADD ./pyproject.toml ./
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Pre commit install
#COPY .pre-commit-config.yaml .
#RUN git init . && pre-commit install-hooks
#RUN pre-commit install

## -- Update system
RUN apt-get update
RUN apt-get install binutils libproj-dev gdal-bin -y
