pipeline {
    agent anySkip to content

Jenkins
CloudCart-CI-CD
#4
Search
Manage Jenkins
dhinimadhu S
Status
Changes
Console Output
Delete build ‘#4’
Git Build Data
Pipeline Overview
Edit build information
Restart from Stage
Replay
Pipeline Steps
Workspaces
Previous Build
Console
Download

Copy
View as plain text
Started by user dhinimadhu S
Obtained Jenkinsfile from git https://github.com/Dhinisha99/CloudCart.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/CloudCart-CI-CD
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/CloudCart-CI-CD/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/Dhinisha99/CloudCart.git # timeout=10
Fetching upstream changes from https://github.com/Dhinisha99/CloudCart.git
 > git --version # timeout=10
 > git --version # 'git version 2.50.1'
 > git fetch --tags --force --progress -- https://github.com/Dhinisha99/CloudCart.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 99369b0f21e77aba2749a99557c49ef9c5800e1f (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 99369b0f21e77aba2749a99557c49ef9c5800e1f # timeout=10
Commit message: "Update Jenkinsfile"
 > git rev-list --no-walk 408505bd9f4f8d9e7edbd4b3ee96ba7fb4d624c2 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Checkout)
[Pipeline] git
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/CloudCart-CI-CD/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/Dhinisha99/CloudCart.git # timeout=10
Fetching upstream changes from https://github.com/Dhinisha99/CloudCart.git
 > git --version # timeout=10
 > git --version # 'git version 2.50.1'
 > git fetch --tags --force --progress -- https://github.com/Dhinisha99/CloudCart.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 99369b0f21e77aba2749a99557c49ef9c5800e1f (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 99369b0f21e77aba2749a99557c49ef9c5800e1f # timeout=10
 > git branch -a -v --no-abbrev # timeout=10
 > git branch -D main # timeout=10
 > git checkout -b main 99369b0f21e77aba2749a99557c49ef9c5800e1f # timeout=10
Commit message: "Update Jenkinsfile"
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] echo
CloudCart source code downloaded successfully!
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Docker Build)
[Pipeline] sh
+ sudo docker build -t cloudcart:latest .

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

For security reasons, the password you type will not be visible.

sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper
sudo: a password is required
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
ERROR: script returned exit code 1
Finished: FAILURE
Jenkins 2.580.2

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dhinisha99/CloudCart.git'
            }
        }

        stage('Build') {
            steps {
                echo 'CloudCart source code downloaded successfully!'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t cloudcart:latest .'
            }
        }
    }
}
