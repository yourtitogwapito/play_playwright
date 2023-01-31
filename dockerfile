FROM python:3.10-slim
WORKDIR /app

#COPY . /app

RUN python -m pip install -r requirements.txt
RUN python -m playwright install --with-deps chromium

EXPOSE 8888
RUN pytest --template=html1/index.html --report=report.html

COPY . /app
CMD ["python", "/app/host-report.py"]
