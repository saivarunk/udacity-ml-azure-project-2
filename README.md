# Operationalizing Machine Learning

This project is part of the Udacity Machine Learning with Azure Nanodegree. In this project, we use Azure ML Studio to train a machine learning model with AutoML, deploy the best model as REST endpoint, and consume it. We also create a AutoML and Endpoint pipeline, publish and consume it using python-sdk.

## Architectural Diagram

![diagram](images/architecture-process.png)

The project mainly has 6 stages:

1. Authentication - We have created a Service Principle (SP) and allow the SP access to ML workspace. This ensures azure cli and Python azure-sdk will be able to access the ML worksapce and manage resources.
2. Creating AutoML Experiment - An AutoML experiment is created using Bankmarketing dataset and relavent compute resources are allocated and with a Exit Criteria.
3. Deploy best performing model - VotingEnsemble Classifier, which was the best performing model of all models generated by AutoML experiement is deployed as an RESTFul service.
4. Enable logging - Logging (Application Monitoring and Insights) is enabled by using a python script logging.py, which uses azure-ml sdk.
5. Consume Best using Model REST endpoint - After model is deployed as an endpoint, it is accesible via secure URL with authentication. Load testing is also performed to analyse the model responsiveness.
6. Create pipeline with AutoML and REST endpoint - A pipeline with AutoML model and REST Endpoint is created using azure-ml python SDK. This is useful in completely automating the model training and deployment process.



## Key Steps



### 1. Authentication

We have created a Service Principle (SP) and allow the SP access to ML workspace. This ensures azure cli and Python azure-sdk will be able to access the ML worksapce and manage resources.

Figure 1 - Creation of Service Principle

![diagram](images/auth-1.jpg)



Figure 2 - Displaying the Service Principle


![diagram](images/auth-2.jpg)



### 2. Creating AutoML Experiment


An AutoML experiment is created using Bankmarketing dataset and relavent compute resources are allocated and with a Exit Criteria.

Figure 3 - Displaying the bankmarketing dataset in ML Studio -> Datasets

![diagram](images/dataset-1.png)


Figure 4 - Bankmarketing dataset is selected while creating AutoML experiment.

![diagram](images/dataset-selection.png)



Figure 4 - Compute specs are provided while creating AutoML experiment

![diagram](images/automl-compute.png)


Figure 5 - Experiment name, Compuet target, Target variable is selected before creating AutoML experiment

![diagram](images/automl-target.png)


Figure 6 - Exit creiteria like training job time, concurrency are configured before creating AutoML experiment

![diagram](images/automl-criteria.png)



Figure 6 - AutoML experiment in creation state.

![diagram](images/auto-ml-0.png)



Figure 7 - AutoML experiment created.

![diagram](images/auto-ml-1.png)



Figure 8 - List of AutoML models created

![diagram](images/auto-ml-2.png)



Figure 9 - Best AutoML model created was VotingEnsemble Classifier

![diagram](images/auto-ml-best.png)



Figure 10 - VotingEnsemble Classifier metrics

![diagram](images/auto-ml-best-metrics.png)



## 3. Deploy best performing model & Enable logging

VotingEnsemble Classifier, which was the best performing model of all models generated by AutoML experiement is deployed as an RESTFul service.

We choose the best model for deployment and enabled "Authentication" while deploying the model using Azure Container Instance (ACI) as compute type.


Figure 11 - Creation of Model Endpoint

![diagram](images/endpoint-creation.png)


Figure 12 - Output from logs.py after enabling Application Monitoring and Insights

![diagram](images/logs.png)



Figure 13 - Endpoint details shwoing Application Monitoring and Insights enabled post logs.py script is executed

![diagram](images/logs-enabled.png)



## 4. Consume Best using Model REST endpoint

After model is deployed as an endpoint, it is accesible via secure URL with authentication. Load testing is also performed to analyse the model responsiveness.

Figure 14 - Swagger documentation running locally showing deployed endpoint specs


![diagram](images/swagger-1.png)



Figure 15 - Swagger documentation running locally showing deployed endpoint specs

![diagram](images/swagger-loan.png)



Figure 16 - Endpoint output from endpoint.py script

![diagram](images/endpoint-op.png)



## Benchmarking

The deployed endpoint is load tested using ab - Apache HTTP benchmarking tool, which will give us statistics on performance of the model interms of concurrency and response times.


Figure 17 - ab benchmarking tool results in the terminal

![diagram](images/benchmark.png)



## 5. Create pipeline with AutoML and REST endpoint


Figure 18 - Notebook for creating Pipelien with AutoML and Model Endpoint

![diagram](images/notebook-1.png)


Figure 19 - Bankmarketing dataset added to Datasets using python sdk

![diagram](images/notebook-dataset.png)


Figure 20 - Notebook showing running state of Pipeline run

![diagram](images/notebook-pipeline-1.png)


Figure 21 - Running state of Pipeline

![diagram](images/pipeline-1.png)


Figure 22 - Notebook showing dataset metrics

![diagram](images/notebook-pipeline-2.png)


Figure 23 - Notebook showing published state of Pipeline endpoint run

![diagram](images/notebook-pipeline-published.png)


Figure 24 - Final state of Pipeline endpoint, with REST endpoint

![diagram](images/pipeline-endpoint.png)


Figure 25 - List of Pipeline Endpoints on Workspace -> Pipelines -> Pipeline Endpoint

![diagram](images/pipeline-endpoint-list.png)



## Screen Recording

[https://www.youtube.com/watch?v=GXHygBldfEg](https://www.youtube.com/watch?v=GXHygBldfEg)



## Standout Suggestions

- One of the suggestion from this AutoML run was the imbalanced data issue which can be observed in Data guardriles section of the experiment run. 
- This can lead to biased prediction, which can affect negatively the model's accuracy.
