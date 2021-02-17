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
          dockerImage = docker.build(imageName)
		  dbImage = docker.image(dbImageName)
         }

      }
    }

    stage('Test versions') {
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
		  /* --network ${n} ./app.py */
  		  /* withDockerNetwork{ n -> */
            dbImage.withRun("--name db  -p 5432:5432 -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD") { db ->
			  sh 'docker ps'
			  sh 'docker inspect db'
              dockerImage.inside("--name app") {
                sh 'python3 ./app.py'
              }
			}
          /* } */
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
        sh "docker rmi $imageName:latest"
      }
    }


  }
  environment {
    imageName = 'estets2/python-sql'
	dbImageName = 'postgres'
    dockerImage = ''
    dbImage = ''
    POSTGRES_HOST = '172.17.0.3'
	POSTGRES_SUBNET = '10.5.0.0/16'
    POSTGRES_USER = 'docker'
    POSTGRES_PASSWORD = 'top-sicret'
  }
  post {
    always {
      echo 'Job well done!'
    }

  }
}
