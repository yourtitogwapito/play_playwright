FROM python:3.10-slim


#
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m playwright install --with-deps chromium

WORKDIR /app
COPY . /app

EXPOSE 8888
RUN pytest --template=html1/index.html --report=report.html
CMD ["python", "host_report.py"]
