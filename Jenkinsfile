pipeline {
    agent any

    environment {
        PYTHON = "python3" // Adjust this to python if using Python 2.x
        VENV = "venv"
    }

    stages {
        stage('Checkout Code') {
            steps {
                    // Clone the GitHub repository
                    git branch: 'feature/add-model', url: 'https://github.com/lavanyajain/mlops-ml-model.git'
            }
        }
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
                // Lint all Python files in the model directory
                sh '''
                source ${VENV}/bin/activate
                find model -name "*.py" | xargs pylint
                '''
            }
        }

        stage('Test') {
            steps {
                // Execute tests
                sh '''
                source ${VENV}/bin/activate
                find tests -name "*.py" | xargs pylint
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the model...'
                sh '''
                hash -r
                if [ ! -d "model" ]; then
                    echo "Model directory does not exist, aborting deployment."
                    exit 1
                fi
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
