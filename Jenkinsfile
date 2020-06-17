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
       stage('Static code metrics') {
           steps {
                echo "Code Coverage"
                sh 'pip install pycobertura'
                sh  ''' source activate ${BUILD_TAG}
                        coverage run irisvmpy/iris.py 1 1 2 3
                        python -m coverage xml -o ./reports/coverage.xml
                    '''
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
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
                    mail to: 'bsnani7@gmail.com',
                        subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                        body: "build has result success if you want to see the reports please see this link: ${BUILD_URL}/testReport"
                    mail to: 'Tzahy92@gmail.com',
                        subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                        body: "build has result success if you want to see the reports please see this link: ${BUILD_URL}/testReport"
                    mail to: 'matanlazimi@gmail.com',
                        subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                        body: "build has result success if you want to see the reports please see this link: ${BUILD_URL}/testReport"
                    mail to: 'yahel.fri@gmail.com',
                        subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                        body: "build has result success if you want to see the reports please see this link: ${BUILD_URL}/testReport"
                }
                failure {
                    mail to: 'bsnani7@gmail.com',
                        subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                        body: "build has result failure if you want to see the reports please see this link: ${BUILD_URL}/testReport "
                }
           }
       }//stage


   } //Stages
} //Pipeline
