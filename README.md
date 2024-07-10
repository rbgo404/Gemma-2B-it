# Gemma-2B-it
Gemma, a family of lightweight, state-of-the-art open models by Google, inherits the same advanced research and technology as the Gemini models. These text-to-text, decoder-only large language models come in English variants, offering open weights, pre-trained versions, and fine-tuned options. Gemma excels in various text generation tasks like question answering, summarization, and reasoning. Their compact size enables deployment in resource-constrained environments like laptops, desktops, or personal cloud setups, democratizing access to cutting-edge AI models and fostering innovation for all.

---
## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the app.py according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

---
## Quick Start
Here is a quick start to help you get up and running with this template on Inferless.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Create a Custom Runtime in Inferless
To access the custom runtime window in Inferless, simply navigate to the sidebar and click on the **Create new Runtime** button. A pop-up will appear.

Next, provide a suitable name for your custom runtime and proceed by uploading the **inferless-runtime-config.yaml** file given above. Finally, ensure you save your changes by clicking on the save button.

### Add Your Hugging Face Access Token
Go into the `inferless.yaml` and replace `<hugging_face_token>` with your hugging face access token. Make sure to check the repo is private to protect your hugging face token.

### Add Your Inferless NFS Volumes Path
Go into the `inferless.yaml` and replace `<your_nfs_volume>` with your NFS volume mount path. Make sure to check the repo is private to protect your NFS volume mount path.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

Select the PyTorch as framework and choose **Repo(custom code)** as your model source and use the forked repo URL as the **Model URL**.

After the create model step, while setting the configuration for the model make sure to select the appropriate runtime.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/git-custom-code/git--custom-code) for more information on model import.

---
## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.
```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
                "inputs": [
                    {
                    "data": [
                        "How to count all the stars in the night sky?"
                    ],
                    "name": "prompt",
                    "shape": [
                        1
                    ],
                    "datatype": "BYTES"
                    }
                ]
                }'
```

---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](https://docs.inferless.com/model-import/input-output-schema) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting to `None`.
```python
def finalize(self):
    self.llm = None
```

For more information refer to the [Inferless docs](https://docs.inferless.com/).