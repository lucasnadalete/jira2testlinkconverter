# __Executing the command__

Pre-requirements: Python 2.7+
Execute the command with the following parameters:

Linux:

    - jira2testlinkconverter --jirafile=<path_jira_file.xml> --reqfile=<path_requirement_file.xml>

Windows:

    jira2testlinkconverter.exe --jirafile=<path_jira_file.xml> --reqfile=<path_requirement_file.xml>

The JIRA file must be exported in XML format using the following sample JQL in the Search for Issues JIRA feature.

    JQL:  project = "<project_name> and Sprint = "<spring_name>" and issuetype = Story

Note: To execute the command is necessary to have write permission in directory.

# __Build project with PyInstaller__

## Creating venv and preparing environment
    python3.x -m venv venv/
    source venv/bin/activate
    pip install -r dependencies.txt (needs to be in the jira2testlinkconverter project folder)

## Windows build command
##### See: http://sparkandshine.net/en/build-a-windows-executable-from-python-scripts-on-linux/
##### Execute:
    wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile jira2testlinkconverter.spec

## Linux build command
##### Execute:
    pyinstaller --onefile jira2testlinkconverter.spec