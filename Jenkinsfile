pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\abhinav.kurup\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'cicd-token', url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git', branch: 'main'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat '"%PYTHON_PATH%" -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r "ICL Automation\\requirements.txt"
                    pip install -e "ICL Automation"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest --alluredir=allure-results
                '''
            }
        }

        stage('Archive Allure Results') {
            steps {
                archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
