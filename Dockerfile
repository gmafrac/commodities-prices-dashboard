FROM confluentinc/cp-kafka:latest

# Adicione o script wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/bin/wait-for-it.sh
RUN chmod +x /usr/bin/wait-for-it.sh

# Verifique o caminho do kafka-topics.sh e defina como uma variável de ambiente
ENV KAFKA_TOPICS_SCRIPT=/usr/bin/kafka-topics.sh

# Copie o script entrypoint para o container
COPY create-topics.sh /usr/bin/create-topics.sh
RUN chmod +x /usr/bin/create-topics.sh

ENTRYPOINT ["/usr/bin/create-topics.sh"]
