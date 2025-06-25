pipeline {
    agent any

    tools {
        // Reference to tools configured in Jenkins > Global Tool Configuration
        allure 'AllureCommandline'
        python 'Python312' // Name of Python tool in Jenkins (adjust if named differently)
    }

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'cicd-token',
                    url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git',
                    branch: 'main'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat 'python --version'
                bat 'python -m venv %VENV_DIR%'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r "ICL Automation\\requirements.txt"
                    pip install -e "ICL Automation"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    if exist allure-results (rmdir /s /q allure-results)
                    call %VENV_DIR%\\Scripts\\activate
                    pytest "ICL Automation\\tests" --alluredir=allure-results || exit /b 0
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
