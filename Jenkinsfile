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
                    junit 'reports/junit.xml'
                        recordIssues(
                            tool: pep8(pattern: 'reports/pep8.report'),
                            unstableTotalAll: 400,
                            failedTotalAll: 400
                        )
                        recordIssues(
                            tool: pyLint(pattern: 'reports/pylint.report'),
                            unstableTotalAll: 400,
                            failedTotalAll: 400
                        )
		                recordIssues(tools: [flake8(pattern: 'reports/pyflakes.report')])
		                //mail to: 'bsnani7@gmail.com', subject: "Status of pipeline: ${currentBuild.fullDisplayName}", body: "build has result ${currentBuild.result} click this link to view the test results: ${BUILD_URL}/testReport"
                }
                success {
                    mail to: 'bsnani7@gmail.com','Tzahy92@gmail.com',
                        subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                        body: "build has result success if you want to see the reports please see this link: ${BUILD_URL}/testReport"
                }
                failure {
                    mail to: 'bsnani7@gmail.com','Tzahy92@gmail.com',
                        subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                        body: "build has result failure if you want to see the reports please see this link: ${BUILD_URL}/testReport "
                }

           }
       }//stage


   } //Stages
} //Pipeline
