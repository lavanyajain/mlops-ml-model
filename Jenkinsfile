pipeline {
    agent any
    environment {
        PYTHONUNBUFFERED = "1"
    }
    stages {
        stage('Setup') {
            steps {
                sh 'python -m pip install numpy scikit-learn pytest pylint'
            }
        }
        stage('Lint') {
            steps {
                sh 'pylint model/*.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying model...'
                sh 'mkdir -p deployment'
                sh 'cp -r model deployment/model'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf deployment'
        }
    }
}
