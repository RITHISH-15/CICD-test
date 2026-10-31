# Automated CI/CD Pipeline for Containerized Flask Application Using Jenkins, Docker file & Podman

A hands-on DevOps project demonstrating how to manage source code, build container images, publish images to a container registry, and automate application workflows using Jenkins and Podman.

## Project Overview

This project containerizes a Python Flask web application and demonstrates a CI/CD workflow using Jenkins, Dockerfile and Podman.

The application is maintained in GitHub. Jenkins retrieves the latest source code, and Podman builds the container image using the Dockerfile. The image can then be published to a container registry and pulled for deployment.

## Architecture

```text
       Developer
           |
           v
      GitHub Repository
           |
           v
         Jenkins
      (Source Checkout)
           |
           v
       Dockerfile
           |
           v
    Podman Image Build
           |
           v
    Container Registry
           |
           v
      Podman Pull
           |
           v
   Flask Application
      (Container)
           |
           v
     Web Browser
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web application framework |
| Dockerfile | Container image instructions |
| Docker | Containerization concepts and image format |
| Podman | Image building and container management |
| Jenkins | CI/CD automation |
| Git & GitHub | Version control and source code management |
| Container Registry | Image storage and distribution |
| Linux (RHEL) | Hosting and execution environment |

## Project Features

- Flask web application containerization.
- Dockerfile-based image creation.
- Automated source code checkout from GitHub using Jenkins.
- Container image building using Podman.
- Container registry integration for image publishing.
- Container execution and verification.
- Linux-based container management.

## Repository Structure

```text
CICD-test/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/RITHISH-15/CICD-test.git
cd CICD-test
```

### 2. Build the container image

Using Podman:

```bash
podman build -t thirukkural-app:v1 .
```

### 3. Verify the image

```bash
podman images
```

### 4. Run the application

```bash
podman run -d \
  --name thirukkural-app \
  -p 5000:5000 \
  thirukkural-app:v1
```

### 5. Access the application

Open the following URL in your browser:

```text
http://localhost:5000
```

## Jenkins Integration

Jenkins is used to automate the source code checkout and container image build process.

Basic workflow:

1. Jenkins connects to the GitHub repository.
2. Jenkins checks out the latest source code.
3. Podman builds the application image using the Dockerfile.
4. The generated image is verified.
5. The image can be published to a configured container registry.
6. The published image can be pulled and deployed using Podman.

## Container Registry Operations

Tag the image with your registry address:

```bash
podman tag thirukkural-app:v1 REGISTRY/USERNAME/thirukkural-app:v1
```

Log in to the registry:

```bash
podman login REGISTRY
```

Push the image:

```bash
podman push REGISTRY/USERNAME/thirukkural-app:v1
```

Pull the image:

```bash
podman pull REGISTRY/USERNAME/thirukkural-app:v1
```

Replace the registry and username placeholders with your actual registry details.

## What I Learned

- Understanding Dockerfile instructions and container image layers.
- Building and managing container images using Podman.
- Integrating GitHub with Jenkins.
- Automating container image build operations.
- Working with container registries.
- Running and verifying containerized applications on Linux.
- Understanding the practical CI/CD workflow.

## Future Improvements

- Automate registry publishing through Jenkins.
- Implement automated application testing.
- Configure webhook-based builds on GitHub commits.
- Automate container deployment after image retrieval.
- Add application health checks and monitoring.

## Author

**Rithish Kumaran A**
