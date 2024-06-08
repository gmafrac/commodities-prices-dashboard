# commodities-prices-dashboard

This project has been made for the college subject SSC0158 - Computação em Nuvem e Arquitetura Orientadas a Serviços (2024). For this reason, our group made a Cloud Application which we use the Kafka to build a real-time streaming data. In this scenario, the theme of this project is the commoddities price.
 
## Group members:
* Guilherme Mafra da Costa - 11272015
* João Alexandro Ferraz - 11800441
* Matheus Baptistella - 11223117

## Project
In this project, we have the producer being responsible to receive the current price of a commodity from a API and send it to the Kafka. Then, the consumer receive the values from the Kafka and store this data into a MongoDB database. At the end, the frontend application plot a real time graph with a time series that show the values stored in the database.  

We have implemented a docker-compose to make this project a containerized application. So, you can run this project through the docker-compose up.
