# faas-ocr-demo

# Simple Automation Demo using Dataloop.ai Python SDK to create a simple Function as a Service (FaaS) for OCR

In this repository you will find the code samples and dataset files needed to go from start to finish covered by [these video demonstrations](https://app.guidde.co/share/playlists/hdmN19SmnZjuCw81zazzZq?origin=4cXRgiQFJqZCWFXQkELs2EkPq182&t=0)

Before you try this at home….please be sure you have the following prerequisites sorted:

1. Working knowledge of Python
2. Python 3.6 or greater installed and validated
3. PIP3 installed and validated
4. DTLPY - the Dataloop SDK - installed and validated
5. Your favorite Python IDE set up with an empty project
6. Dataloop.ai subscription with at least a Pro subscription package
- See the Subscription page accessible via the Dataloop.ai console
7. Have a user on a Dataloop.ai account with Owner or Developer role
8. Verify that this user can log into the Dataloop.al platform via DTLPY
9. Have a second user on your Dataloop.ai account to use as an Annotator in the Labeling task assignment
10. Download the files from these folders in this repository:
- Sample Code[sample dataset here](https://github.com/dataloop-ai-apps/faas-ocr-demo/tree/main/dataset%20files)
- [Sample Dataset Files](https://github.com/dataloop-ai-apps/faas-ocr-demo/tree/main/dataset%20files)

The [video demonstrations](https://app.guidde.co/share/playlists/hdmN19SmnZjuCw81zazzZq?origin=4cXRgiQFJqZCWFXQkELs2EkPq182&t=0) will walk you through the following:

- Create Project
  - name is `Class with Attributes Example`
  - Add Annotator from another domain
- Create a Dataset
  - Name it `OCR demo dataset`
  - Create a Recipe (aka Ontology) for a catalog
  - Catalog consists of Labels (aka classes) and Attributes
  - 1111
    - AAAA
    - BBBB
    - CCCC
  - 2222
    - XXXX
    - YYYY
    - ZZZZ
  - We will not be covering Section and Instructions - defaults will suffice
- Create and load a Function as a Service (FaaS) that uses OCR on text files to automatically extract data
- Create a Pipeline
  - Add a Data step and point to OCR demo dataset
  - Add a Workflow step that creates a Task and with a Labeling Assignment
  - Add FaaS step that leverages the OCR FaaS you created and loaded
  - Add a Workflow step that creates a Task and with a QA Assignment
  - Execute the pipeline
- Navigate to the Dataset you created previously and upload dataset files from the [sample dataset here](https://github.com/dataloop-ai-apps/faas-ocr-demo/tree/main/dataset%20files)
- Log out and log in as an Annotator user
  - Locate and complete the Labeling Assignment
- Log out and log in with Owner or Developer user
  - Navigate to Tasks then the Assignment
  - Find and view OCR extracted in data in a file
  - Complete the QA Assignment
- Check Pipeline status
- Pause the Pipeline
- Export the JSON file that contains the annotation data

Good luck and please leave stars or feedback letting us know how things went for you.
