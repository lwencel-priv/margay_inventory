FROM python:3.10-slim as base
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN pip install --no-cache-dir -r /project/requirements.txt
COPY ./app /project/app

FROM base as production
ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--host", "0.0.0.0", "--port", "80"]
