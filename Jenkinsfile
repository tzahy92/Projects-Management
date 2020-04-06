pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('build_1') {
            steps {
                sh 'python --version'
            }
        }
        stage('build') {
            steps {
            sh 'pip install -r requirements.txt'
            }
        }
         stage('test') {
             steps {
                sh 'python manage test'
             }
        }
    }
}
