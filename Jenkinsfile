pipeline {
    agent any

    tools {
        allure 'AllureCommandline' // Must match name configured in Jenkins > Global Tool Configuration
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
                bat 'dir'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"C:\\Users\\samarth.madalageri\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv'
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

        stage('Install Framework (Editable Mode)') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    cd "ICL Automation"
                    pip install -e .
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    cd "ICL Automation"
                    pytest -s tests/dummy_test --alluredir=reports\\allure-results || exit 0
                '''
            }
        }

        stage('Archive Allure Report') {
            steps {
                archiveArtifacts artifacts: 'ICL Automation/reports/allure-results/**', allowEmptyArchive: true
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'ICL Automation/reports/allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo 'Pipeline complete.'
        }
    }
}
