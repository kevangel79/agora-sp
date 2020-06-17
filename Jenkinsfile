pipeline {
    agent any
    options {
        checkoutToSubdirectory('agora-sp')
    }
    environment {
        PROJECT_DIR="agora-sp"
    }
    stages {
        stage ('Run Tests') {
            steps {
                echo 'Building Rpm...'
                sh '''
                    cd $WORKSPACE/$PROJECT_DIR
                    docker-compose up -d
                    scl enable rh-python36 bash
                    cd tests/selenium_tests
                    pip install requirements.txt
                    echo "Wait for argo container to initialize"
                    while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/ui/auth/login)" != "200" ]]; do sleep 5; done
                    python agora_ui_tests.py --url http://localhost:8000/
                '''
            }
            post {
                always {
                    cleanWs()
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            script{
                if ( env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'devel' ) {
                    slackSend( message: ":rocket: New version for <$BUILD_URL|$PROJECT_DIR>:$BRANCH_NAME Job: $JOB_NAME !")
                }
            }
        }
        failure {
            script{
                if ( env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'devel' ) {
                    slackSend( message: ":rain_cloud: Build Failed for <$BUILD_URL|$PROJECT_DIR>:$BRANCH_NAME Job: $JOB_NAME")
                }
            }   
        }
    }
}