FROM python:3.10-slim

WORKDIR /app

COPY ./requirements/requirements.txt .
COPY ./core_code ./core_code

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "-m", "core_code"]