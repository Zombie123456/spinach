FROM python:3.9
WORKDIR /app/
COPY . /app/
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]