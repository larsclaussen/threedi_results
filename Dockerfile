FROM python:3.6.6-stretch

WORKDIR /srv

COPY requirements_dev.txt requirements.txt  /srv/

RUN pip3 install --no-cache-dir -r requirements.txt && pip3 install -r /srv/requirements_dev.txt

EXPOSE 8000

CMD python /srv/threedi_results/threedi_results.py

