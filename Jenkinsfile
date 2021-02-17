def withDockerNetwork(Closure inner) {
  try {
    networkId = UUID.randomUUID().toString()
    sh "docker network create ${networkId}"
    inner.call(networkId)
  } finally {
    sh "docker network rm ${networkId}"
  }
}

pipeline {
  agent any
  stages {
    stage('Building image') {
      steps {
        script {
          dockerImage = docker.build imagename
          dockerDatabase = docker.build dbgename
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
		
		  withDockerNetwork{ n ->
            dockerDatabase.withRun("--network ${n} -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASS") { db ->
              dockerImage.inside("--network ${n}") {
                sh 'python3 ./app.py'
              }
			}
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
	dbgename = 'postgres'
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
