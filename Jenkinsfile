properties ([
        parameters ([
            string(defaultValue: '', description: '', name : 'user_id')
        ])
])

pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    // triggers {
    //     pollSCM '* * * * *'
    // }
    stages {
        stage('Login') {
                steps {
                    echo "Active user is now ${params.user_id}"
                }
        }
        
        stage('Build') {
            steps {
                echo "Building.."
                // input 'Continue to next stage?'
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Brad
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
