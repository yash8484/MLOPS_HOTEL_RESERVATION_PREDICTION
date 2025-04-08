pipeline{
    agent any

    stages {
        stage('cloning Github repo to Jenkins') {
            steps {
                script{
                echo 'cloning Github repo to jenkins...'
                git branch: 'main', credentialsId: 'github-token', url: 'https://github.com/yash8484/MLOPS_HOTEL_RESERVATION_PREDICTION.git'
                }
            }
        }
    }
}

    
    
