// pipeline {
//   agent any

// //   environment {
// //     OPENAI_API_KEY = credentials('openai-api-key')
// //   }

//   stages {
//     stage('Checkout') {
//       steps {
//         checkout([
//           $class: 'GitSCM',
//           branches: [[name: 'refs/heads/main']],
//           doGenerateSubmoduleConfigurations: false,
//           extensions: [],
//           userRemoteConfigs: [[url: 'https://github.com/Mr3bd/promfoo2025.git']]
//         ])
//       }
//     }

//     stage('Set Up Virtual Environment') {
//       steps {
//         bat 'python -m venv venv'
//       }
//     }

//     stage('Install Dependencies') {
//       steps {
//         bat '''
//           call .\\venv\\Scripts\\activate.bat
//           pip install --upgrade pip
//           pip install -r requirements.txt
//         '''
//       }
//     }

//     stage('Run Flask App in Background') {
//       steps {
//         bat '''
//           call .\\venv\\Scripts\\activate.bat
//           start /B python chatbot_api.py
//         '''
//         sleep time: 15, unit: 'SECONDS'
//       }
//     }

//     stage('Run Promptfoo Tests') {
//       steps {
//         bat '''
//           call .\\venv\\Scripts\\activate.bat
//           .\\venv\\Scripts\\promptfoo.exe eval --config promptfooconfig.yaml
//         '''
//       }
//     }
//   }

//   post {
//     always {
//       echo 'Pipeline finished.'
//     }
//   }
// }










pipeline {
    agent any

    stages {
        stage('Checkout') {
          steps {
            checkout([
              $class: 'GitSCM',
              branches: [[name: 'refs/heads/main']],
              doGenerateSubmoduleConfigurations: false,
              extensions: [],
              userRemoteConfigs: [[url: 'https://github.com/Mr3bd/promfoo2025.git']]
            ])
          }
        }

        stage('Docker Compose Up') {
            steps {
                script {
                    bat 'docker-compose down'     // Clean up any old containers
                    bat 'docker-compose build'    // Build updated image
                    bat 'docker-compose up --abort-on-container-exit' // Wait for promptfoo eval
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            bat 'docker-compose down'
        }
    }
}
