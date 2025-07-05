pipeline {
  agent any
  environment {
    IMAGE_NAME     = "fastapi-jenkins"       // Name of the Docker image
    CONTAINER_NAME = "fastapi_app"           // Name of the running container
    APP_PORT       = "8000"                  // Port exposed by app
  }
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/Akhil-317/CICD-lab.git', credentialsId: 'github-pat'
      }
    }
    stage('Build Image') {
      steps {
        sh 'docker build -t $IMAGE_NAME .'   // Build Docker image
      }
    }
    stage('Replace Container') {
      steps {
        sh '''
          docker stop $CONTAINER_NAME || true   # Stop if running
          docker rm   $CONTAINER_NAME || true   # Remove old container
          docker run -d --name $CONTAINER_NAME -p $APP_PORT:$APP_PORT $IMAGE_NAME   # Run new container
        '''
      }
    }
  }
  post {
    success {
      echo "✅ Deployment succeeded; app is live on port $APP_PORT"
    }
    failure {
      echo "❌ Deployment failed; check logs"
    }
  }
}
