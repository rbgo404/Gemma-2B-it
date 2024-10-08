import os
import sys

class InferlessPythonModel:
    def initialize(self):
        repo_id = "google/gemma-2b-it" # Specify the model repository 
        
    def infer(self,inputs):
        prompts = inputs["prompt"]  # Extract the prompt from the input
        # result = self.llm.generate(prompts, self.sampling_params)
        # Extract the generated text from the result
        # result_output = [output.outputs[0].text for output in result]
        
        # Return a dictionary containing the result
        sys.exit()
        return

    def finalize(self):
        pass
