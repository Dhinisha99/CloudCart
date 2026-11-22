pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dhinisha99/CloudCart.git'
            }
        }

        stage('Build') {
            steps {
                echo 'CloudCart source code downloaded successfully!'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t cloudcart:latest .
                '''
            }
        }

        stage('ECR Login') {
            steps {
                sh '''
                    aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 763103708879.dkr.ecr.ap-south-1.amazonaws.com
                '''
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                    docker tag cloudcart:latest 763103708879.dkr.ecr.ap-south-1.amazonaws.com/cloudcart:latest

                    docker push 763103708879.dkr.ecr.ap-south-1.amazonaws.com/cloudcart:latest
                '''
            }
        }
    }
}