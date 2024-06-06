FROM python:3.9-slim

WORKDIR .

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]