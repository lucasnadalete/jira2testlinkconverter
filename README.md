# Download Docker compose
curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-testlink/master/docker-compose.yml > docker-compose.yml
# Start Bitnami Testlink Docker Image
docker-compose up -d
# Updating the latest image of Testlink Docker
docker pull bitnami/testlink:latest

# Converters:
- Pre-requirements: Python 2.7+
- The JIRA file must be exported in XML format using the following sample JQL in the Search for Issues JIRA feature.
```sql
JQL:  project = "<project_name> and Sprint = "<spring_name>" and issuetype = Story
```
                
## For Windows use:
1. Download the [converter version](jira2testlinkconverter-windows.zip) for Windows
2. Extract the file with the executable file and templates directory
3. Execute the command: 
```bash
jira2testlinkconverter.exe --jirafile=<path_jira_file.xml> --reqfile=<path_requirement_file.xml>
```
Note: To execute the command is necessary to have write permission in directory.

## For Linux use:
1. Download the [converter version](jira2testlinkconverter-linux.zip) for Linux
2. Extract the file with the executable file and templates directory
3. Execute the command: 
```bash
./jira2testlinkconverter --jirafile=<path_jira_file.xml> --reqfile=<path_requirement_file.xml>
```
Note: To execute the command is necessary to have write permission in directory.
