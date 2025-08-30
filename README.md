# Text2Test - BDD Test Automation Framework

**Academic Thesis Project - University "Politehnica" of Bucharest (2022)**

Testing Framework that implements BDD through Gherkin syntax and makes use of predefined keywords to generate web automated test cases using PyTest and Selenium Webdriver.

## About This Project

This framework was developed as part of my Computer Science thesis to address the gap between business stakeholders and technical teams in BDD implementation. The research included surveys with 10 IT professionals and validation testing that confirmed the need for automated test generation from Gherkin scenarios.

## Academic Context

- **Institution**: University "Politehnica" of Bucharest
- **Degree**: Computer Science and Information Technology  
- **Year**: 2022
- **Research Focus**: Behavior-driven development automation and stakeholder collaboration

## Research Validation

- Surveyed 10 IT professionals in the testing domain
- 100% confirmed need for automated test case generation
- Average usability score: 8.2/10
- Time reduction: From weeks to hours for test creation cycles

## Installation

Download locally the git repository.

Install the prerequisites in the "requirements.txt" file.

Run commands:
```bash
Function runtext2test {python "path\to\controller.py" $args}
Set-Alias -Name text2test -Value runtext2test
```

## Usage

Create feature files inside the "features" folder.

### Example Feature File

```gherkin
Feature: run a login test case with background

Background:
    Given we open WEBSITE 'https://www.amazon.com/'

Scenario: login
    When we CLICK 'user_name'
    And we TYPE 'user_name' 'uname'
    And we CLICK 'password'
    And we TYPE 'password' 'pass'
    And we CLICK 'submitForm'
    Then an ERROR 'ERRORMSG' 'Invalid username password combination' will be raised
```

### Available Keywords

- **WEBSITE** + 'link': opens the link
- **CLICK** + 'id': clicks on the specified element
- **TYPE** + 'id' + 'text': types text into the specified element
- **TITLE** + 'text': verifies title is equal to text
- **SCREENSHOT** + 'name': takes screenshot and saves it as name
- **ERROR** + 'id' + 'text': verifies the error with id is equal to text

Feel free to update the 'code.json' file to add keywords suited to your specific needs.

### Command Line Usage

```bash
text2test [-t|all|run|h] [--help]
```

**Options:**
- `h`: Print this Help
- `help`: Print this Help
- `t`: Generate a test from a specific feature file
- `all`: Generate tests from all feature files inside features folder
- `run`: Execute generated test cases and generate a report

## Known Limitations

As an academic proof-of-concept:
- Limited keyword database (expandable via code.json)
- Basic error handling
- Designed for demonstration purposes
- Tested primarily on Windows 10

## Future Academic Directions

Based on thesis research and user feedback:
- API testing support
- Multi-threading capabilities
- Extended browser compatibility
- Performance testing integration
- UI management interface

## Academic References

This project implements concepts from behavior-driven development research and addresses challenges identified in large-scale software testing literature.

## License

MIT License - see LICENSE file for details

## Contact

For academic inquiries or collaboration: ovidiuandy@gmail.com
