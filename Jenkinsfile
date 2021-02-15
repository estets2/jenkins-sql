pipeline {
	environment {
		imagename = "estets2/python-sql"
		dockerImage = ''
	}
	agent any
	checkout scm
	stages {
		stage('Building image') {
			steps{
				script {
					dockerImage = docker.build imagename
				}
			}
		}
		stage('Test image') {
			steps {
				script {
					dockerImage.inside {
						sh 'psql --version'
					}
				}
			}
		}
		stage('Remove Unused docker image') {
			steps {
				sh "docker rmi $imagename:latest"
			}
		}
	}
}
