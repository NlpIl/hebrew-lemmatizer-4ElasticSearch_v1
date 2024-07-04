# For more information, please refer to https://aka.ms/vscode-docker-python
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create directories
WORKDIR /code

# Install requirements
ENV DEBIAN_FRONTEND="noninteractive" 
RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Copy code
COPY src/ .

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd appuser && mkdir -p /home/appuser/.cache
RUN chown -R appuser . && chown -R appuser /home/appuser
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8002"]
