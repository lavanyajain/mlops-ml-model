pipeline {
    agent any

    environment {
        PYTHON = "python3"
        VENV = "venv"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'feature/add-model', url: 'https://github.com/lavanyajain/mlops-ml-model.git'
            }
        }

        stage('Check Environment') {
            steps {
                sh '''
                echo "Checking the working directory and its contents..."
                pwd
                ls -la
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                ${PYTHON} -m pip install --upgrade pip
                ${PYTHON} -m pip install virtualenv
                ${PYTHON} -m virtualenv ${VENV}
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                source ${VENV}/bin/activate
                pip install numpy scikit-learn pytest pylint
                '''
            }
        }

        stage('Prepare Directories') {
            steps {
                echo 'Ensuring all directories exist...'
                sh '''
                mkdir -p model
                mkdir -p tests
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Linting Python files in the model directory...'
                sh '''
                source ${VENV}/bin/activate
                find model -name "*.py" | xargs pylint
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                source ${VENV}/bin/activate
                pytest tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the model...'
                sh '''
                source ${VENV}/bin/activate
                if [ -d "model" ]; then
                    mkdir -p deployment
                    cp -r model deployment/model
                else
                    echo "Model directory does not exist, aborting deployment."
                    exit 1
                fi
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh '''
            rm -rf ${VENV}
            rm -rf deployment
            '''
        }
    }
}
