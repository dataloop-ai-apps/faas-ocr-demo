# Use the Dataloop.ai platform and Python SDK to create a simple Function as a Service (FaaS) for OCR on .txt files

Ever wonder what it takes to do a little OCR on Text files but don't know where to start?  Well...here's you're answer.  Sign up for an account on the [Dataloop.ai](https://console.dataloop.ai/welcome) platform, upgrade to the Pro package and give this example a try.

**Audience:**  This example is meant for people with a working knowledge of Python, data labeling and QA methods, and that have an Optical Character Recognition (OCR) AI training data creation use case that they need to satisfy.  

**Outcome:**  Once complete, you'll have a basic understanding of what is involved in using the Dataloop.ai platform to build a basic data labeling and QA pipleline that extracts via OCR the values of the labeled data in .txt files in a dataset.  You'll also take away a JSON output file that includes the .txt file metadata as well as the labels and extracted OCR values for you to use to train a model.

In this repository you will find the code samples and dataset files needed to go from start to finish covered by [these video demonstrations](https://app.guidde.co/share/playlists/hdmN19SmnZjuCw81zazzZq?origin=4cXRgiQFJqZCWFXQkELs2EkPq182&t=0)

Before you try this at home….please be sure you have the following prerequisites sorted:

1. Working knowledge of Python
2. Python 3.6 or greater installed and validated
3. PIP3 installed and validated
4. DTLPY - the Dataloop SDK - installed and validated
5. Your favorite Python IDE set up with an empty project
6. **Dataloop.ai subscription with at least a Pro subscription package**
- See the [Subscription page accessible via the Dataloop.ai console](https://console.dataloop.ai/iam/6af0b572-1ff2-46fc-b1ee-d16275c58f7f/account?tab=subscription)
7. Have a user on a Dataloop.ai account with Owner or Developer role
8. Verify that this user can log into the Dataloop.al platform via DTLPY
9. Have a second user on your Dataloop.ai account to use as an Annotator in the Labeling task assignment
10. Download the files from these folders in this repository:
- [Sample Code](https://github.com/dataloop-ai-apps/faas-ocr-demo/tree/main/sample%20code)
- [Sample Dataset Files](https://github.com/dataloop-ai-apps/faas-ocr-demo/tree/main/dataset%20files)

<a href="https://app.guidde.co/share/playlists/hdmN19SmnZjuCw81zazzZq?origin=4cXRgiQFJqZCWFXQkELs2EkPq182&t=0" rel="some text">![Video Demonstrations](http://www.google.com.au/images/nav_logo7.png)</a>

The [video demonstrations](https://app.guidde.co/share/playlists/hdmN19SmnZjuCw81zazzZq?origin=4cXRgiQFJqZCWFXQkELs2EkPq182&t=0) will walk you through the following:

- Create Project
  - name is `Class with Attributes Example`
  - Add Annotator from another domain
- Create a Dataset
  - Name it `OCR demo dataset`
  - Create a Recipe (aka Ontology) for a catalog
  - Catalog consists of Labels (aka Classes) and Attributes
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
