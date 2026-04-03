pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Install & Lint') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pip install flake8'
        sh 'flake8 .'
      }
    }
    stage('Test') { steps { sh 'pytest -q' } }
    stage('Docker Build') { steps { sh 'docker build -t aceest-fitness .' } }
  }
}

