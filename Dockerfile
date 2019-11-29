FROM python:3.7
RUN mkdir -p /business_logic
WORKDIR /business_logic
COPY . /business_logic
EXPOSE 9020
RUN pip install -r requirements.txt
CMD ["python", "server.py"]