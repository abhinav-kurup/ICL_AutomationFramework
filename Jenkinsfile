pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        WORK_DIR = 'ICL Automation'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git', branch: 'shivamkonkar'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    source venv/bin/activate
                    cd "ICL Automation"
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    cd "ICL Automation"
                    pytest -s tests/demo --alluredir=reports/allure-results || true
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
