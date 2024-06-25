FROM python:3.10-slim

WORKDIR /app

RUN pip install virtualenv

RUN virtualenv venv

RUN . venv/bin/activate && pip install --upgrade pip

COPY requirements.txt .

RUN . venv/bin/activate && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash", "-c", ". venv/bin/activate && exec python main.py"]
