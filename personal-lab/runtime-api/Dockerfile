FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r personal-lab/runtime-api/requirements.txt
EXPOSE 8080
CMD ["python","personal-lab/runtime-api/run.py"]
