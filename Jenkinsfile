pipeline{
    agent any

    Environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('cloning Github repo to Jenkins') {
            steps {
                script{
                echo 'cloning Github repo to jenkins...'
                git branch: 'main', credentialsId: 'github-token', url: 'https://github.com/yash8484/MLOPS_HOTEL_RESERVATION_PREDICTION.git'
                }
            }
        }

        stage('Setting up our Virtual Environment and Installing Dependencies') {
            steps {
                script{
                echo 'Setting up our Virtual Environment and Installing Dependencies...'
                sh '''
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -e .
                '''
                }
            }
        }
    }
}
    
    
