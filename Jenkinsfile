pipeline {
	environment {
		imagename = "estets2/python-sql"
		dockerImage = ''
	}
	agent any
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
						sh 'python3 --version'
						sh 'pip3 --version'
						sh 'pip3 freeze'
					}
				}
			}
		}

		stage('Push docker image') {
			steps {
				docker.withRegistry('https://registry.hub.docker.com', '97bad7f7-5fa5-42ef-a13e-595d2884a1f1') {
					dockerImage.push("latest")
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
