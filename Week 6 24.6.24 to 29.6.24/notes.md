# AZURE storage tutorial

Video link :- https://www.youtube.com/watch?v=UzTtastcBsk&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=Mjg2NjY&feature=emb_logo

Azure storage offer massively scalable object store for **data objects**, a file system service for the cloud, a messaging store for reliable messaging and a NoSQL store.

Azure storage is :
- durable
- secure
- scalable
- managed
- accesible

![alt text](<Screenshot (835).png>)

## Blob Storage

Blob storage provides flat hierarchy of files.

![](<Screenshot (836).png>)

### Blob storage Access tier

Azure storage provides different options for accessing block blob based data based on usage patterns.

- Hot : optimized for frequent access to objects
- Cool : optimized for storing large amounts of data that is infrequently accessed and stored for at least 30 days

- Archive : optimized for data that can tolerate several hours of retrieval latency and will remain in the Archive tier for at least 180 days.

## File Storage

Managed file shares for cloud or on-promises deployments.

![alt text](<Screenshot (837).png>)

## File vs Blob storage

![alt text](<Screenshot (838).png>)

## Storage Queue

A messaging store for reliable messaging between application components.

![alt text](<Screenshot (839).png>)

## Table Storage

A NoSQL store for schemaless storage of structured data.

![alt text](<Screenshot (840).png>)

### Storage performance tier

General purpose storage accounts may be configured either for the following performance tiers :-

- A **standard** performance tier for storing blob, files, tables, queues, and Azure virtual machine disks.

- A **premium** performance tier for storing unmanaged virtual machine disks only.

## Data redundancy

Azure storage replicates multiple copies of our data.

Replication options for a storage account include :-
- Locally-redundant storage (**LRS**)
- Zone-redundant storage (**ZRS**)
- Geo-redundant storage (**GRS**)
- Read-access geo-redundant storage (**RA-GRS**)

### Locally-redundant storage(**LRS**)

![alt text](<Screenshot (841).png>)

### Zone-redundant storage (**ZRS**)

![alt text](<Screenshot (842).png>)

### Geo-redundant storage (**GRS**)

![alt text](<Screenshot (843).png>)

### Read-access geo-redundant storage (**RA-GRS**)

![alt text](<Screenshot (844).png>)

