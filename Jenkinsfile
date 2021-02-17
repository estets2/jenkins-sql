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


    stage('Run App') {
      steps {
        script {
		  /* --network ${n}  -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD */
  		  /* withDockerNetwork{ n -> */
            dbImage.withRun("--name db  -p 5432:5432 -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD") { db ->
			  sh 'docker inspect db| grep IPAddress'
              dockerImage.inside("--name app") {
                sh 'psql --version'
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip3 freeze'
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
    POSTGRES_USER = 'docker'
    POSTGRES_PASSWORD = 'docker12'
  }
  post {
    always {
      echo 'Job well done!'
    }

  }
}
