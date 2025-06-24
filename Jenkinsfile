pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git', branch: 'main'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat '"C:\\Users\\abhinav.kurup\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv'
            }
        }

        stage('Activate & Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pip install -r "ICL Automation\\requirements.txt"
                pip install -e "ICL Automation"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest -s "ICL Automation\\tests\\demo" --alluredir="ICL Automation\\reports\\allure-results"
                '''
            }
        }

        stage('Archive Allure Results') {
            steps {
                archiveArtifacts artifacts: 'ICL Automation/reports/allure-results/**', allowEmptyArchive: true
            }
        }
    }
}
