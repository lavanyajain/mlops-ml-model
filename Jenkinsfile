pipeline {
    agent any

    environment {
        PYTHON = "python3" // Adjust this to python if using Python 2.x
        VENV = "venv"
    }

    stages {
        stage('Setup Environment') {
            steps {
                // Setup Python virtual environment
                sh '''
                ${PYTHON} -m pip install --upgrade pip
                ${PYTHON} -m pip install virtualenv
                ${PYTHON} -m virtualenv ${VENV}
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary Python packages
                sh '''
                source ${VENV}/bin/activate
                pip install numpy scikit-learn pytest pylint
                '''
            }
        }

        stage('Lint') {
            steps {
                // Perform lint checks on Python code
                sh '''
                source ${VENV}/bin/activate
                pylint model/*.py
                '''
            }
        }

        stage('Test') {
            steps {
                // Execute tests
                sh '''
                source ${VENV}/bin/activate
                pytest tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                // Simulate deployment steps
                sh '''
                source ${VENV}/bin/activate
                mkdir -p deployment
                cp -r model deployment/model
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf ${VENV}'
            sh 'rm -rf deployment'
        }
    }
}
