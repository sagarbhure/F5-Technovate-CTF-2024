FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir PyPDF2

CMD ["python3", "/app/pdf.py"]
