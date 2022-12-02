FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
WORKDIR /code/app
EXPOSE 50010
ENV PYTHONPATH "/code/app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "50010"]