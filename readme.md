# GCP Project README

This README document provides an overview of a project that demonstrates working with Google Cloud Platform (GCP). The project involves setting up a GKE cluster, developing a simple Flask app, creating a Dockerfile for the app, and implementing a CI/CD pipeline using Cloud Build. Additionally, two separate environments, namely production and development, are created within the GKE cluster.

## Project Overview

The project showcases a standard workflow for deploying a containerized application on GCP. It utilizes various GCP services such as GKE, Cloud Build, and Container Registry to achieve efficient development, testing, and deployment processes. 

## Project Steps

1. ### GKE Cluster Creation
   First, a GKE (Google Kubernetes Engine) cluster is created to provide a managed Kubernetes environment for deploying and managing containerized applications.

2. ### Flask App Development
   A simple Flask application is developed as an example application to be deployed on the GKE cluster.

3. ### Dockerfile Creation
   A Dockerfile is created to define the environment and dependencies required to run the Flask application within a container.

4. ### Branching Strategy
   Different branches are used for best practices, such as separating development and production environments.

5. ### Environment Setup
   Two environments, namely development and production, are created within the GKE cluster to separate the deployment stages and ensure proper testing before moving to production.

6. ### CI/CD Pipeline Implementation
   A CI/CD pipeline is implemented using Cloud Build. This pipeline is triggered automatically upon pushing changes to the development repository.

7. ### cloudbuild.yaml Configuration
   The cloudbuild.yaml file is configured to build the container image, push it to the GCR (Google Container Registry), and deploy the container as a deployment with a load balancing service in the development environment, according to the provided YAML file.

8. ### Deployment to Production
   After verifying that everything is working correctly in the development environment, the development branch is merged into the main branch, triggering the CI/CD pipeline again, but this time for the production environment.
