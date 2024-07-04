if [ -z "$MY_HOST_PERMISSION" ]; then
  echo "No permission string provided.Using defualt permission dicta:8000"
  else
  # Path to the policy file
  POLICY_FILE="./elasticsearch/plugin.policy"
  echo "grant {" >> $POLICY_FILE
  echo "    permission java.net.URLPermission \"$MY_HOST_PERMISSION\", \"POST:Accept,Content-Type\";" >> $POLICY_FILE
  echo "};" >> $POLICY_FILE
  echo "Permission added to policy file."
fi


gradle -b plugin-lemmas/build.gradle bundlePlugin
cp plugin-lemmas/build/distributions/heb-lemmas-plugin-1.0-SNAPSHOT.zip elasticsearch/

gradle -b plugin-stopwords/build.gradle bundlePlugin
cp plugin-stopwords/build/distributions/heb-stopwords-plugin-1.0-SNAPSHOT.zip elasticsearch/

sudo docker compose -f docker-compose-3d.yml down
sudo rm -rf ./data
sudo mkdir ./data
sudo mkdir ./data/elastic
sudo chown -R $USER:$USER .
sudo chmod -R 777 ./data/elastic
sudo docker compose -f docker-compose-3d.yml build
sudo docker compose -f docker-compose-3d.yml up -d --remove-orphans
