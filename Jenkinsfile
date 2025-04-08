pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Cloning GitHub repo') {
            steps {
                echo 'Cloning GitHub repo...'
                git branch: 'main', credentialsId: 'github-token', url: 'https://github.com/yash8484/MLOPS_HOTEL_RESERVATION_PREDICTION.git'
            }
        }

        stage('Set up Virtual Environment & Install Dependencies') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                '''
            }
        }
    }
}
