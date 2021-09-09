FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip3 install flask
RUN pip3 install requests
RUN chmod +x /app/app.py
CMD ["python3", "app.py"]
