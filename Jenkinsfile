pipeline {
	environment {
		imagename = "estets2/python-sql"
		dockerImage = ''
	}
	stages {
		agent any
		checkout scm
		stage('Building image') {
			steps{
				script {
					dockerImage = docker.build imagename
				}
			}
		}
		stage('Test image') {
			steps {
				dockerImage.inside {
					sh 'psql --version'
				}
			}
		}
		stage('Remove Unused docker image') {
			steps{
				sh "docker rmi $imagename:latest"
			}
		}
	}
}
