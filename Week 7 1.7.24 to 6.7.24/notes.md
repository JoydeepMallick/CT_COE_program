# Trigers in ADF

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