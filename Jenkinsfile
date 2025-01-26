pipeline {
    agent any  // This specifies that Jenkins can run this pipeline on any agent

    environment {
        // Define environment variables that will be available to all stages
        PYTHONUNBUFFERED = "1"
    }

    stages {
        stage('Preparation') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/yourusername/yourrepo.git'
            }
        }

        stage('Build') {
            steps {
                // This is where you would include your build commands
                echo 'Running build...'
                // For Python, there might not be a 'build' if you aren't compiling, but maybe you're packaging
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Run tests using pytest or another framework
                echo 'Running tests...'
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add commands to deploy your application
                // For example, you might copy files to a server
            }
        }
    }

    post {
        always {
            // Clean up workspace
            deleteDir()
        }
        success {
            // You could add actions that should only happen when the build succeeds
            echo 'Build succeeded!'
        }
        failure {
            // Actions for when the build fails
            echo 'Build failed!'
        }
        unstable {
            // Actions for handling unstable build state
            echo 'Build is unstable.'
        }
    }
}
