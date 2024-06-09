FROM docker.elastic.co/elasticsearch/elasticsearch:8.9.0

COPY plugin.policy /usr/share/elasticsearch/jdk/conf/security/

COPY heb-lemmas-plugin-1.0-SNAPSHOT.zip /usr/share/elasticsearch/
RUN ./bin/elasticsearch-plugin install -b file:///usr/share/elasticsearch/heb-lemmas-plugin-1.0-SNAPSHOT.zip

COPY heb-stopwords-plugin-1.0-SNAPSHOT.zip /usr/share/elasticsearch/
RUN ./bin/elasticsearch-plugin install -b file:///usr/share/elasticsearch/heb-stopwords-plugin-1.0-SNAPSHOT.zip
