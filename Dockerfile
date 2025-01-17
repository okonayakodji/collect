# Got this template from https://habr.com/ru/companies/wunderfund/articles/586778/
# Stage 1
FROM python:3.13-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY Pipfile .

# Changed by me
RUN pip install pipenv && pipenv lock
RUN pipenv requirements > requirements.txt
# End

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Stage 2
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

# TODO(okonayakodji): ENTRYPOINT
