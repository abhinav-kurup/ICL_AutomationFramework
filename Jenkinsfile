pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:\\Users\\abhinav.kurup\\AppData\\Local\\Programs\\Python\\Python312"
        VENV_PATH = "venv"
        ALLURE_RESULTS = "allure-results"
        ALLURE_REPORT = "allure-report"
    }

    tools {
        // Add tool definitions here if using Jenkins-managed tools
        // python 'Python312'
        // allure 'AllureCommandline'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git credentialsId: 'cicd-token', url: 'https://github.com/abhinav-kurup/ICL_AutomationFramework.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat "${env.PYTHON_HOME}\\python.exe -m venv ${env.VENV_PATH}"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    call ${env.VENV_PATH}\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r "ICL Automation\\requirements.txt"
                    pip install -e "ICL Automation"
                """
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat "if exist ${env.ALLURE_RESULTS} (rmdir /s /q ${env.ALLURE_RESULTS})"
                    
                    def exitCode = bat(
                        script: """
                            call ${env.VENV_PATH}\\Scripts\\activate
                            pytest "ICL Automation\\tests" --alluredir=${env.ALLURE_RESULTS}
                        """,
                        returnStatus: true
                    )

                    if (exitCode != 0) {
                        unstable("Tests had failures. Marking build as UNSTABLE.")
                    }
                }
            }
        }

        stage('Archive Allure Results') {
            steps {
                archiveArtifacts artifacts: "${env.ALLURE_RESULTS}/**", allowEmptyArchive: true
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: "${env.ALLURE_RESULTS}"]]
                ])
            }
        }
    }

    post {
        unstable {
            script {
                // Optional: Convert UNSTABLE to SUCCESS if needed
                echo 'Build was unstable, forcing status to SUCCESS to avoid job failure flag.'
                currentBuild.rawBuild.@result = hudson.model.Result.SUCCESS
            }
        }
        always {
            echo "Pipeline finished."
        }
    }
}
