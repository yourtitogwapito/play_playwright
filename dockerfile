FROM python:3.10-slim
WORKDIR /usr/app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt
RUN python -m playwright install --with-deps chromium

COPY . .
RUN pytest --template=html1/index.html --report=report.html
ENTRYPOINT ["python", "src/host-report.py"]
