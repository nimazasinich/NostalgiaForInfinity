FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -c "import py_find_1st; print('Package imported successfully!')"
 
