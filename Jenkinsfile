pipeline {
   agent any
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
   }
}
