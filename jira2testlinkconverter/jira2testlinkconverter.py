import sys
from lxml import etree
import codecs


class Main():

    def __init__(self):
        requirementTemplateFile = open('templates/requirement_template.xml')
        self.req_template = requirementTemplateFile.read()
        requirementTemplateFile.close()
        requirementsTemplateFile = open('templates/requirements_template.xml')
        self.reqs_template = requirementsTemplateFile.read()
        requirementsTemplateFile.close()

    def validationArgs(self, args):
        argsCount = 0
        for arg in args:
            if arg.__contains__('--jirafile') or arg.__contains__('--reqfile'):
                argsCount += 1

        return argsCount == 2

    def extractArg(self, field, args):
        for arg in args:
            if arg.__contains__(field):
                indexSeparator = arg.index('=')
                return arg[indexSeparator + 1:]

    def readJiraXmlFile(self, file):
        root = etree.parse(file)
        requirements = []
        for item in root.iter("item"):
            requirement = self.req_template
            for element in item.iter('*'):
                requirement = requirement.replace('#{}#'.format(element.tag.upper()),
                                                  element.text if element.text != None else '')
            requirements.append(requirement)
        return requirements

    def writeTestlinkXmlFile(self, path, requirements):
        file = codecs.open(path, 'w', encoding='utf-8')
        requirements = self.reqs_template.replace('#REQUIREMENTS#', requirements)
        file.write(requirements)
        file.close()


if __name__ == '__main__':
    m = Main()

    if (m.validationArgs(sys.argv)):
        jiraFilePath = m.extractArg('--jirafile', sys.argv)
        reqFilePath = m.extractArg('--reqfile', sys.argv)
        jiraRequirements = m.readJiraXmlFile(jiraFilePath)
        m.writeTestlinkXmlFile(reqFilePath, ''.join(jiraRequirements))
    else:
        print('''
                Pre-requirements: Python 2.7+
                Execute the command with the following parameters:
                
                    - Linux: jira2testlinkconverter --jirafile=<path_jira_file.xml> --reqfile=<path_requirement_file.xml>
                    - Windows: jira2testlinkconverter.exe --jirafile=<path_jira_file.xml> --reqfile=<path_requirement_file.xml>
                
                The JIRA file must be exported in XML format using the following sample JQL in the Search for Issues JIRA feature.
                
                JQL:  project = "<project_name> and Sprint = "<spring_name>" and issuetype = Story
                
                Note: To execute the command is necessary to have write permission in directory.
                ''')
