pipeline {
    agent any

    environment {
        PYTHON = "python3"
        VENV = "venv"
    }

    tools {
        // Ensure python3 is used if python3 label is available in Jenkins tools configuration
        python 'python3'
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Setup virtual environment
                    sh '''
                    ${PYTHON} -m pip install --upgrade pip
                    ${PYTHON} -m pip install virtualenv
                    ${PYTHON} -m virtualenv ${VENV}
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies within virtual environment
                    sh '''
                    source ${VENV}/bin/activate
                    pip install numpy scikit-learn pytest pylint
                    '''
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    // Perform linting
                    sh '''
                    source ${VENV}/bin/activate
                    pylint model/*.py
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh '''
                    source ${VENV}/bin/activate
                    pytest tests/
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Dummy deployment step
                    echo 'Deploying the model...'
                    sh '''
                    source ${VENV}/bin/activate
                    mkdir -p deployment
                    cp -r model deployment/model
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf deployment'
            sh 'rm -rf ${VENV}'
        }
    }
}
