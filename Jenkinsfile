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
                    docker-compose up -d --build
                    rm requirements*.txt
                    cd tests/selenium_tests
                    pipenv install --python 3.7
                    pipenv install selenium
                    echo "Wait for argo container to initialize"
                    while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/ui/auth/login)" != "200" ]]; do sleep 5; done
                    sleep 10
                    pipenv run python agora_ui_tests.py --url http://localhost:8000/
                '''
            }
            post {
                always {
                    sh '''
                      cd $WORKSPACE/$PROJECT_DIR
                      pipenv --rm
                    '''
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
