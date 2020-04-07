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
                   sh 'pip uninstall bson'
                   sh 'pip uninstall pymongo'
                   sh 'conda install -c anaconda pymongo'
                   sh 'pip install djongo'
                   sh 'pip install dnspython' 
                   sh 'pip install bson'
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
                   sh 'pip uninstall bson'
                   sh 'pip uninstall pymongo'
                   sh 'conda install -c anaconda pymongo'
                   sh 'pip install djongo'
                   sh 'pip install dnspython' 
                   sh 'pip install bson'
                   sh 'python manage.py test'
               }
           }
       }
   }
}
