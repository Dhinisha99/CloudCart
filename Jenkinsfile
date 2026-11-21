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
                sh 'sudo docker build -t cloudcart:latest .'
            }
        }
    }
}
