pipeline {
   agent {
       docker {
            image 'python:3-alpine'
        }
   }
   stages {
       stage('Build') {
           steps {
               withEnv(["HOME=${env.WORKSPACE}"]) {
                   sh 'pip install django'
                   sh 'pip install djongo'
                   sh 'pip uninstall -y bson pymongo && pip install bson==0.5.8 && pip install pymongo==3.10.1'
                   sh 'pip install dnspython'
               }
           }
       }
       stage('Test') {
           steps {
               withEnv(["HOME=${env.WORKSPACE}"]) {
                   sh 'pip install django-jenkins'
                   sh 'pip install pep8'
                   sh 'pip install pyflakes'
                   sh 'pip install pylint'
                   sh 'pip install \'coverage==4.5.4\''
                   sh 'python manage.py jenkins trainer.tests --enable-coverage'
               }
           }
           post{
                always{
                    juint 'PM/reports/juint.xml'
                        recordIssues(
                            tool: pep8(pattern: 'PM/reports/pep8.report'),
                            unstableTotalAll: 400,
                            failedTotalAll: 400
                        )
                        recordIssues(
                            tool: pyLint(pattern: 'PM/reports/pylint.report'),
                            unstableTotalAll: 400,
                            failedTotalAll: 400
                        )
		                recordIssues(tools: [flake8(pattern: 'PM/reports/pyflakes.report')])

                }
           }
       }


   } //Stages
} //Pipeline
