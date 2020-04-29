# FROM alpine:3.10

# COPY LICENSE README.md /

# COPY entrypoint.sh /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]



FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH=/app
CMD ["/app/main.py"]
