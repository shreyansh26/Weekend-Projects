# docker build -t iris-ml-v2 .
# docker run -d -p 8000:8000 --name iris-api-v2 iris-ml-v2

FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]