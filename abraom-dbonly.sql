
DROP DATABASE if exists abraom;

CREATE DATABASE abraom
  WITH OWNER postgres
  CONNECTION LIMIT -1;

\connect abraom;

DROP TABLE if exists variants;
