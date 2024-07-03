# Triggers in ADF

Video link :- https://www.youtube.com/watch?v=LFdROd_jhaI&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt


- Triggers help execute pipeline
- they determine when a pipeline execution needs to be kicked off.
- pipelines and triggers have **many to many relationship**(**except the tumbling window trigger**)

- **multiple triggers can kick of a single pipeline or a single trigger can kick off multiple pipelines**.

#### demo link :- https://youtu.be/LFdROd_jhaI?t=134

## Types of triggers

### 1. Schedule trigger 
trigger that invokes a pipeline on a wall clock schedule
### 2. Tumbling Window trigger
trigger that operates on a periodic interval  while also retaining state
### 3. Event based trigger
a trigger that responds to a event.






## Schedule trigger in ADF

Video link :- https://www.youtube.com/watch?v=YqpmDtG8WpI&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

- These trigger that invokes a pipeline on a wall clock schedule
- supports periodic and advanced calendar options

e.g. triggers support intervals likely weekly or like monday at 5pm and thursday at  9 am

#### Demo link :- https://youtu.be/YqpmDtG8WpI?t=118








## Tumbling windows trigger in ADF

Video link :- https://www.youtube.com/watch?v=vvuq-C_NXLI&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

- Types of trigger that fire at a periodic time interval from a specified start time, while retaining state

- **one to one relationship with a pipeline and can only reference a singular pipeline.**


#### Demo link :- https://youtu.be/vvuq-C_NXLI?t=65


### Advantages
- can create trigger dependencies
- can create self dependent triggers also
- we have access to windows start time and window end time values using below system properties
    1. `trigger().outputs.windowStartTime`
    2. `trigger().outputs.windowEndTime`

#### Demo link :- https://youtu.be/vvuq-C_NXLI?t=306 



### Tumbling windows trigger dependency in ADF

Video link :- https://www.youtube.com/watch?v=8X4CGsIuxGg&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

- In order to build dependency chain and make sure that the trigger is executed only after successful excecution of another trigger using Tumbling Window  Trigger dependency feature.

**NOTE** :-
A Tumbling Window  Trigger can depend on maximum 2 other triggers

- We have access to windows start time and window end time values using below system properties
    1. `trigger().outputs.windowStartTime`
    2. `trigger().outputs.windowEndTime`


#### Example demo link :- https://youtu.be/8X4CGsIuxGg?t=70


⭐Important link :- https://learn.microsoft.com/en-us/azure/data-factory/tumbling-window-trigger-dependency

## Self dependency trigger
dependent on its own. We have to provide offset for this in negative only.

#### demo link :- https://youtu.be/8X4CGsIuxGg?t=776

## Event based trigger in ADF

Video link :- https://www.youtube.com/watch?v=RXEHrET9dUc&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

- runs pipelines in response to an event, such as arrival of a file, or the deletion of a file, in **Azure Blob Storage**

- data integration scenarios often require Data Factory customers to trigger pipeline based on events such as the arrival or deletion of a file in your Azure Storage account.

- Data factory is now integrated with **Azure Event Grid**, which lets you trigger pipelines on  an event.

#### demo link :- https://youtu.be/RXEHrET9dUc?t=119



### Azure Event Grid

- allows you to respond to events happening  at different types of Azure and non-Azure services in real time fashion.

### Event based trigger properties

- `@triggerBody().folderPath`
- `@triggerBody().fileName`

#### demo link :- https://youtu.be/RXEHrET9dUc?t=538








# Integration runtime in ADF

Video link:- https://www.youtube.com/watch?v=8rJ0mvAswfc

The **Integration Runtime(IR)** is the compute infrastructure used by ADF to provide following data integration capabilities across different network environment :-

- Data flow :  execute a data flow in managed azure compute environment

- Data movement : copy data across data stores in public network and private network

- Activity Dispatch : dispatch and monitor transformation activities running on a variety of compute activities.

- SSIS Package execution : Execute SQL  Server Integration Services(SSIS) packages in a managed Azure  compute environment.

#### demo link :- https://youtu.be/8rJ0mvAswfc?t=307

#### read more [HERE](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime)

### Types of Integration runtimes

Data Factory offers three types of Integration Runtime (IR), and you should choose the type that best serves your data integration capabilities and network environment requirements. The three types of IR are:

- Azure
- Self-hosted
- Azure-SSIS

IR type	|Public Network Support	|Private Link Support
--------|-----------------------|------------
Azure	|Data Flow, Data movement, Activity dispatch	|Data Flow, Data movement, Activity dispatch
Self-hosted	|Data movement, Activity dispatch |Data movement, Activity dispatch
Azure-SSIS	|SSIS package execution	|SSIS package execution


The following diagram shows the location settings for Data Factory and its integration runtimes:
![](https://learn.microsoft.com/en-us/azure/data-factory/media/concepts-integration-runtime/integration-runtime-location.png)

see video from here:- https://youtu.be/8rJ0mvAswfc?t=678

⭐⭐Read this blog :- https://jorgklein.com/2017/09/26/azure-data-factory-and-ssis-better-together-with-adf-v2-preview/

![](https://jorgklein.com/wp-content/uploads/2017/09/different-integration-runtimes1.png)

see demo :- https://youtu.be/8rJ0mvAswfc?t=838










# Azure Integration Runtime in ADF

Video link :- https://www.youtube.com/watch?v=MQ84n4Al_p4&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt


- Azure Integration Runtime is capable of performing below in public network.
    - Running Dataflows
    - Running Copy Activities  between cloud stores
    - running **transform activities**

- Azure Integration runtime supports connecting to data stores and computer services with public accessible endpoints.

- Azure integration runtime provides fully managed, serverless compute in Azure

- Azure IR elastically scaled up accordingly without we having  to explicitly   adjusting size of the Azure Integration Runtime.

#### demo link : https://youtu.be/MQ84n4Al_p4?t=163

- Azure integration runtime will come by default with location as `auto-resolve`


### Creating Azure integration runtime

We only need to create an Azure IR when we would like to explicitly define the location of IR or if we want to virtually group the activity executions on different IRs for management purpose.

#### demo link :- https://youtu.be/MQ84n4Al_p4?t=482





# Self hosted integration runtime in ADF

video link :- https://www.youtube.com/watch?v=Rl1b-pRO4LE&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

### ⭐⭐[read here](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime?tabs=data-factory)

![](https://learn.microsoft.com/en-us/azure/data-factory/media/create-self-hosted-integration-runtime/high-level-overview.png)

demo link :- https://youtu.be/Rl1b-pRO4LE?t=267










# Shared Self Hosted Integration runtime in Azure Data Factory

video link :- https://www.youtube.com/watch?v=9BvU_NpntSg&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt






# Shared Self Hosted Integration runtime in Azure Data Factory

video link : https://www.youtube.com/watch?v=9BvU_NpntSg&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=OTY3MTQ&feature=emb_imp_woyt