FROM python

RUN mkdir /app

COPY . /app

RUN python -m pip install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python","route.py"]
