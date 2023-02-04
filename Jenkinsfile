pipeline {
    agent any
    stages {
        stage("Install dependencies") {
            steps {
                echo 'Install dependencies'
                pip install -r requirements.txt
            }
        }

        stage("run tests"){
            steps {
                echo 'Running tests'
                behave tests/features/hiberus/hiberus_page.feature
            }

        }

        stage("Reporting results"){
            steps {
                echo 'Last step'
            }
        }
    }
}