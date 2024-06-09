# commodities-prices-dashboard

This project was developed for the college course `SSC0158 - Computação em Nuvem e Arquitetura Orientada a Serviços (2024)`. Our group created a cloud application using Kafka to build a real-time streaming data pipeline focused on commodity prices.

## Group members:
* Guilherme Mafra da Costa - 11272015
* João Alexandro Ferraz - 11800441
* Matheus Baptistella - 11223117

## Project
In this project, a producer retrieves current commodity prices from an API and sends this data to Kafka. The consumer then receives the data from Kafka and stores it in a MongoDB database. Finally, the frontend application displays a real-time graph with a time series showing the stored values.

We have implemented a Docker Compose setup to containerize this application. You can run the project using the following command:

```
docker-compose build && docker-compose up
```

After this, you can acess the web site in the localhost:6053.

