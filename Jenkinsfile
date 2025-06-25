pipeline {
    agent any

    environment {
        PYTHON_HOME = tool name: 'Python312', type: 'jenkins.plugins.shiningpanda.tools.PythonInstallation'
    }

    tools {
        allure 'AllureCommandline'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'cicd-token', url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git', branch: 'main'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat '"%PYTHON_HOME%\\python.exe" -m venv venv'
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
                    if exist allure-results (rmdir /s /q allure-results)
                    call venv\\Scripts\\activate
                    pytest --alluredir=allure-results || exit /b 0
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
