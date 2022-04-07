FROM python:3.10-slim as base
RUN pip install tox

FROM base as build
COPY . /inventory
WORKDIR /inventory
RUN tox -e mypy,build

FROM python:3.10-slim
COPY --from=base /inventory/tox_files/dist/* /opt/
RUN pip install /opt/*.whl
EXPOSE 5000
ENTRYPOINT inventory
