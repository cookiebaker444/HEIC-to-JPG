# Use older Ubuntu version as base image
FROM ubuntu:20.04

# Set non-interactive mode to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install dependencies
RUN apt update && apt install -y \
    libheif-dev \
    libde265-dev \
    python3 \
    python3-pip \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Explicitly set the user as root (default)
USER root

RUN mkdir /app

# Set working directory
WORKDIR /app

# Copy Python script into the container
COPY convert_heic_to_jpg.py /app/

# Install Python packages globally
RUN pip3 install pillow pillow-heif

# Run the script directly
CMD ["python3", "convert_heic_to_jpg.py"]
