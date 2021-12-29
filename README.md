# Infrastructure Automation

Connect to remote servers through SSHv2 protocol and execute pre-defined commands.\
Can be used for software provisioning, configuration management, and application-deployment enabling infrastructure as code.  
It runs on many Unix-like systems, and can configure both Unix-like systems as well as Microsoft Windows.

## Pre-requisites
Set appropriate values in -
- [ip.txt](https://github.com/abrasham-chowdhury/InfrastructureAutomation/blob/main/resources/ip.txt) - IP addresses of servers to establish connection (Use new line for each address)
- [credentials.txt](https://github.com/abrasham-chowdhury/InfrastructureAutomation/blob/main/resources/credentials.txt) - Credentials for servers (comma separated value - username,password)
- [cmd.txt](https://github.com/abrasham-chowdhury/InfrastructureAutomation/blob/main/resources/cmd.txt) - Commands to execute (User new line for each command)

## Run
- python network_app.py

## Dependency
- [Paramiko](https://www.paramiko.org/)
