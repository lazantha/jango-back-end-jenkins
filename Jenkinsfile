pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }

        stage('Build docker') {
            steps {
                echo 'Building Docker file ...'
            }
        }

        stage('Engaging kubernetes') {
            steps {
                echo 'Building kubernetes file ...'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
