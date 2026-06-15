pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Start Appium') {
            steps {
                bat 'start /B appium'
                bat 'timeout /t 5 /nobreak'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/report.html', allowEmptyArchive: true
            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
        }
    }
}
