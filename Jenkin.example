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
                script {
                    def result = bat(
                        script: """
                            if exist allure-results (rmdir /s /q allure-results)
                            call ${VENV_DIR}\\Scripts\\activate
                            pytest "ICL Automation\\tests" --alluredir=allure-results
                        """,
                        returnStatus: true
                    )
                    if (result != 0) {
                        currentBuild.result = 'UNSTABLE'
                        echo "Some tests failed. Marking build as UNSTABLE."
                    }
                }
            }
        }

        stage('Archive Allure Results') {
            when {
                expression { fileExists('allure-results') }
            }
            steps {
                archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
            }
        }

        stage('Publish Allure Report') {
            when {
                expression { fileExists('allure-results') }
            }
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
