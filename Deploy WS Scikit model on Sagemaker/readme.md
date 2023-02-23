This folder explains how to deploy a sci-kit learn model trained on a watson studio platform using demand response prediction file.

Folder Structure: <br>
**1. [Deploy WS Sci-kit model.ipynb](https://github.com/IBM/watson-studio-sagemaker-watson-trust-integration/blob/main/Deploy%20WS%20Scikit%20model%20on%20Sagemaker/Deploy%20WS%20Sci-kit%20model.ipynb)** notebook contains instructions on how to deploy the model on Amazon Sagemaker using an inference script.<br>
**2. scikit_model.pkl**: Pickle file of demand response prediction model exported from the CPD project.<br>
**3. inference.py**: An entry point script which contains following functions. <br>
`input_fn()` - Takes request data and deserializes the data into an object for prediction.  <br>
`output_fn()` - Takes the result of prediction and serializes this according to the response content type.  <br>
`predict_fn()` - Function that takes the deserialized request object and performs inference against the loaded model.  <br>
`model_fn()` - Function to load the model.  <br>
Additional information on model loading and model serving for scikit-learn on SageMaker can be found in the [SageMaker Scikit-learn Model Server documentation](https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/using_sklearn.html#deploy-a-scikit-learn-model). <br>
**4. DemandResponseHoldout.csv:** Holdout data to test scoring on the endpoint created on Sagemaker.
