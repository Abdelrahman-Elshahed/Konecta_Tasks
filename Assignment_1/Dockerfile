FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY model/ ./model/
COPY data/ ./data/

EXPOSE 8501

# Set environment variables
ENV PYTHONPATH=/app

# Run the application
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]