pipeline {
   agent none
   stages {
       stage('Build') {
           agent {
               docker {
                   image 'python:3-alpine'
               }
           }
           steps {
               withEnv(["HOME=${env.WORKSPACE}"]) {
                   sh 'pip install django'
                   sh 'pip install djongo'
                   sh 'pip uninstall -y bson pymongo && pip install bson==0.5.8 && pip install pymongo==3.10.1'
                   sh 'pip install dnspython'
                   sh 'pip install django-jenkins'
               }
           }
       }
       stage('Test') {
           agent {
               docker {
                   image 'python:3-alpine'
               }
           }
           steps {
               withEnv(["HOME=${env.WORKSPACE}"]) {
                   sh 'pip install django'
                   sh 'pip install djongo'
                   sh 'pip uninstall -y bson pymongo && pip install bson==0.5.8 && pip install pymongo==3.10.1'
                   sh 'pip install dnspython'
                   sh 'pip install django-jenkins'
                   sh 'python manage.py test'
               }
           }
       }
      stage('LightHouse'){
         // Generate your lighthouse report.
         agent{
            steps{
               node {
                  sh 'npx lighthouse-ci https://www.example.com --jsonReport --report=.'
                  lighthouseReport('./report.json')
               }

               //Generate your lighthouse report with specific report name
               node {
                  sh 'npx lighthouse-ci https://www.example.com --jsonReport --report=.'
                  lighthouseReport file: './report.json', name: 'My Report'
               }
            }
         }
      }
   }
}
