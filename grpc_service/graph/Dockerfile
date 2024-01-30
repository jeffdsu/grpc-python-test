FROM python:3.11


WORKDIR /usr/src/app

RUN pip install poetry
COPY . .

RUN poetry config virtualenvs.create false


# Install project dependencies
RUN poetry install --no-dev  # Omit '--no-dev' if you want development dependencies


CMD uvicorn schema:app --host "0.0.0.0"
