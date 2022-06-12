FROM python:3.9


WORKDIR /code/build
# RUN apt update -y && apt install nettools -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH /code/build/app

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000", "--reload"]
