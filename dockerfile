FROM python:3.11-slim
 
COPY ./requirements.txt /requirements.txt
 
RUN pip install --upgrade -r /requirements.txt
 
COPY . .

EXPOSE 9000
 
CMD ["uvicorn", "--app-dir=/src", "app:app", "--host", "0.0.0.0", "--port", "9000"]