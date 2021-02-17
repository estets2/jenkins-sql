pipeline {
  agent any
  stages {
    stage('Building image') {
      steps {
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

    stage('Run App') {
      steps {
        script {
          dockerImage.inside {
            sh 'python3 ./app.py'
          }
        }
      }
    }
    
    stage('Push docker image') {
      steps {
        script {
          docker.withRegistry('', 'dockerhub') {
            dockerImage.push("latest")
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
  environment {
    imagename = 'estets2/python-sql'
    dockerImage = ''
	POSTGRES_HOST = '172.17.0.3'
    POSTGRES_USER = 'docker'
    POSTGRES_PASS = 'top-sicret'
  }
  post {
    always {
      echo 'Job well done!'
    }

  }
}
