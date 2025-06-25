# messaging_app/Dockerfile

# 1. Use official Python base image
FROM python:3.10

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set working directory
WORKDIR /app

# 4. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy project files into the container
COPY . .

# 6. Expose port
EXPOSE 8000

# 7. Default command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
