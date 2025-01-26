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
                echo 'Installing project dependencies...'
                sh '''
                source ${VENV}/bin/activate
                pip install numpy scikit-learn pytest pylint
                '''
            }
        }

        stage('Ensure Directories Exist') {
            steps {
                echo 'Ensuring that all necessary directories exist...'
                sh '''
                mkdir -p model
                mkdir -p tests
                '''
            }
        }

        stage('Check Tests Directory') {
            steps {
                echo 'Verifying the existence of test files...'
                sh '''
                if [ ! -d "tests" ] || [ -z "$(ls -A tests)" ]; then
                    echo "No tests directory or no test files found. Test stage skipped."
                    exit 1
                else
                    echo "Test files found."
                    find tests -name "test_*.py" -or -name "*_test.py"
                fi
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Linting Python files...'
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
            echo "Clean up complete."
            '''
        }
    }
}
