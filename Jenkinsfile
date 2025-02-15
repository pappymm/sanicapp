pipeline {
    agent any
    environment {
        // Set Minikube's Docker environment
        MINIKUBE_DOCKER_ENV = sh(script: 'minikube docker-env', returnStdout: true).trim()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/pappymm/sanicapp.git',
                        credentialsId: 'your-git-credentials-id'
                    ]]
                ])
            }
        }
        stage('Setup Minikube Docker Environment') {
            steps {
                script {
                    // Ensure Minikube is running
                    sh 'minikube status || minikube start'
                    // Set up Minikube's Docker environment
                    sh '''
                        eval ${MINIKUBE_DOCKER_ENV}
                        docker images
                    '''
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        eval ${MINIKUBE_DOCKER_ENV}
                        docker build -t pappymm/sanicapp:latest .
                    '''
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
    post {
        failure {
            echo 'Pipeline failed! Check the logs for details.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
