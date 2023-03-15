# Monitor AWS Sagemaker model using IBM Watson Openscale 
## Introduction

This project shows how to monitor a model deployed on AWS Sagemaker for quality, bias and explainability, using IBM Watson Openscale on the IBM Cloud Pak for Data platform.  You can leverage both AWS Sagemaker and IBM Cloud Pak for Data platforms to bring a machine learning model from development to production with maximum flexibility, and then monitor the health and performance of the deployed models with Watson OpenSCale. 

Monitor AWS Sagemaker model using IBM Watson Openscale project picks up the endpoint of a machine learning model deployed on AWS Sagemaker and uses the endpoint generated to monitor with Watson OpenScale. 

Before proceeding to the instructions, make sure a model is deployed on AWS Sagemaker. The sample notebooks [here](https://github.com/IBM/WatsonStudio-Sagemaker-Integration) demonstrates how to deploy a model on AWS Sagemaker 

Then import the [notebook](https://github.com/IBM/WatsonStudio-Sagemaker-Integration/blob/main/Monitor%20AWS%20Sagemaker%20model%20using%20IBM%20Watson%20Openscale/monitor-sagemaker-model-with-watson-openscale.ipynb) and the [data asset](https://github.com/IBM/WatsonStudio-Sagemaker-Integration/blob/main/Monitor%20AWS%20Sagemaker%20model%20using%20IBM%20Watson%20Openscale/demandresponseinput.csv) into [CPDaaS platform](https://dataplatform.cloud.ibm.com/home2?context=cpdaas)

Once the import is completed follow the below instructions. 
## Instructions
Follow these steps to implement the project:
1. Navigate to the project, select the **Assets** tab and scroll to the **Source Code** section.
1. Edit the  **monitor-sagemaker-model-with-watson-openscale** notebook by clicking the three dots next to the notebook name and choose Edit option. Follow the instructions in the notebook to configure and step through running it.




### Sample Data Asset
Below file can be found in the project's data  area:
- [demandresponseinput.csv](https://github.com/IBM/WatsonStudio-Sagemaker-Integration/blob/main/Monitor%20AWS%20Sagemaker%20model%20using%20IBM%20Watson%20Openscale/demandresponseinput.csv):  CSV file containing customers demographic, personal and historic energy usage information. This file was used to train demand response model.

## Notebooks

**[monitor-sagemaker-model-with-watson-openscale](https://github.com/IBM/WatsonStudio-Sagemaker-Integration/blob/main/Monitor%20AWS%20Sagemaker%20model%20using%20IBM%20Watson%20Openscale/monitor-sagemaker-model-with-watson-openscale.ipynb)**: <br>
Provide these required inputs in the first few cells to run the notebook: <br>

- IBM Cloud API key<br>
- AWS Sagemaker Credentials and the model name deployed on Sagemaker. <br>
- DB2 or IBM Cloud Object Storage credentials for the storage repository where you will store sample training data. <br>


Then run the notebooks step-by-step. <br>
 This notebook performs the following functions: <br>
    
1. Fetch the Sagemaker model and deployments using the AWS credentials provided. <br>
2. Configure the Watson OpenScale service using the IBM Cloud Pak for Data credentials. <br>
3. Define the Service Provider and Subscription for AWS Sagemaker model on Watson Openscale.<br>
4. Set up the Quality monitor: Watson Openscale sets an alert threshold for the model and shows an alert on the dashboard if the model accuracy measurement (area under the curve, in the case of a binary classifier) falls below this threshold. <br>
5. Set up a Fairness monitor: Watson OpenScale helps in detection of Bias at run time. It monitors the data which has been sent to the model as well as the model prediction (Payload data). It then identifies bias in a specified column. In our example we use gender column to check bias.<br>
6. Set up Explanations: Watson OpenScale provides LIME-based and Contrastive explanations for the specified transactions. Explanations monitor shows the top features influencing the model's prediction. 


