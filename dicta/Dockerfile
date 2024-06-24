# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11.9-slim-bookworm

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create directories
WORKDIR /code

# Install requirements
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
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8000"]
