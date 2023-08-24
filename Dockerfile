# Stage 1: Build Stage
FROM python:3.10 AS builder

# Set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev


# Copy the poetry.lock and pyproject.toml files to the container
COPY pyproject.toml poetry.lock /app/


# Install project dependencies using Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi


# Copy the rest of the application code to the container
COPY . .
