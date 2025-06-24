pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        WORK_DIR = 'ICL Automation'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git', branch: 'main'
            }
        }

        stage('Debug Python') {
            steps {
                bat 'where python'
                bat 'python --version'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat '''
                python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                cd "ICL Automation"
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                cd "ICL Automation"
                pytest -s tests/demo --alluredir=reports/allure-results || exit 0
                '''
            }
        }

        stage('Archive Allure Results') {
            steps {
                archiveArtifacts artifacts: "ICL Automation/reports/allure-results/**", allowEmptyArchive: true
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: "ICL Automation/reports/allure-results"]]
            }
        }
    }
}
