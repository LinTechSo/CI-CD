pipeline {
    agent none
    stages {
        stage('Test on Development Environ'){
            agent {
                docker {
                    label 'master'
                    image 'python:3.7-alpine'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python test.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
        stage('Deploy If Test Succeded'){          
            agent {
                    label 'parham'
            }
            when {
                expression {env.GIT_BRANCH == 'origin/master'}
            }
            steps {
		        sh './install.sh'
                sh 'docker build -t helloapp .'
                sh 'docker run -itd helloapp:latest'
            }
            post {
	            failure {
                    echo 'Failed Build Beacause of Test stage'
                }
            }
        }
    }
}
