pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
         stage('test') {
             steps {
                sh 'python trainer/tests.py'
             }
        }
    }
}
