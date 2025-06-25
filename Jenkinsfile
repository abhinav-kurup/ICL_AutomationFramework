pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\abhinav.kurup\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git(
                    url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git',
                    branch: 'main',
                    credentialsId: 'cicd-token'
                )
            }
        }

        stage('Setup Python Env') {
            steps {
                bat "${PYTHON} -m venv ${VENV_DIR}"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r "ICL Automation\\requirements.txt"
                    pip install -e "ICL Automation"
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    if exist allure-results (rmdir /s /q allure-results)
                    call ${VENV_DIR}\\Scripts\\activate
                    pytest "ICL Automation\\tests" --alluredir=allure-results
                """
            }
        }

        stage('Archive Allure Results') {
            steps {
                archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        unstable {
            echo '⚠️ Some tests failed. Build marked as UNSTABLE.'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
