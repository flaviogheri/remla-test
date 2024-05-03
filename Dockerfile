# Dockerfile
FROM python:3.7.17-slim
WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r requirements.txt
COPY app.py /root/
ENTRYPOINT ["python"]
CMD ["app.py"]