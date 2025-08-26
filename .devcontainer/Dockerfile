# Base image with Sphinx preinstalled
FROM sphinxdoc/sphinx

# Ensure proper locale support (needed for German special characters)
ENV LC_ALL=C.UTF-8

# Install additional OS packages for Git and SSH (e.g., needed by VS Code extensions)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    git \
    openssh-client \
 && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /docs

# Install Python dependencies for building documentation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
