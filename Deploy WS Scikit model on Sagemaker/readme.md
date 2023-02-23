This folder explains how to deploy an auto ai model trained on a demand response prediction file on Cloud Pak for data 4.5.x.

Folder Structure: <br>
**1. [Deploy WS Sci-kit model.ipynb](https://github.ibm.com/Vikram-Bhat1/AutoAI-Sagemaker/blob/main/Scikit_Sagemaker/Deploy%20WS%20Sci-kit%20model.ipynb)** notebook contains instructions on how to deploy the model on Amazon Sagemaker using an inference script.<br>
**2. scikit_model.pickle**: Pickle file of demand response prediction model exported from the CPD project.<br>
**3. inference.py**: An entry point script which contains following functions. <br>
`input_fn()` - Takes request data and deserializes the data into an object for prediction.  <br>
`output_fn()` - Takes the result of prediction and serializes this according to the response content type.  <br>
`predict_fn()` - Function that takes the deserialized request object and performs inference against the loaded model.  <br>
`model_fn()` - Function to load the model.  <br>
Additional information on model loading and model serving for scikit-learn on SageMaker can be found in the [SageMaker Scikit-learn Model Server documentation](https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/using_sklearn.html#deploy-a-scikit-learn-model). <br>
**4. requirements.txt:** It installs additional Python dependencies required to run inference script. <br>
**5. DemandResponseHoldout.csv:** Holdout data to test scoring on the endpoint created on Sagemaker.