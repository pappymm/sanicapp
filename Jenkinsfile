pipeline {
    agent any
    stages {
        stage('Start Minikube') {
            steps {
                script {
                    sh '''
                        minikube status || minikube start
                    '''
                }
            }
        }
        stage('Set Minikube Docker') {
            steps {
                script {
                    sh '''
                        eval $(minikube docker-env)
                    '''
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        docker build -t pappymm/sanicapp:latest .
                    '''
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f kubernetes/deployment.yaml'
                }
            }
        }
    }
    post {
        failure {
            echo 'Pipeline failed! Check the logs for details.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
    }
}

