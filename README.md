# hawk-eye
Distributed system to track objects or faces from images.

### Requirements:

  - Cockroach DB: 
https://www.cockroachlabs.com

  - Open CV:
https://opencv.org/


### To start cockroach node:

  - In the first node:

  ```bash
    > cockroach start --insecure --host=<first-node-ip>
  ```

  - In other nodes (the join node ip must be some node already running):

  ```bash
    > cockroach start --insecure --host=<this-node-ip> --join=<first-node-ip>:26257
  ```

  - Create databases

  ```bash
    > cockroach sql --insecure
    root@:26257/> CREATE DATABASE tracking;
    root@:26257/> CREATE TABLE tracking.faceBank  (id SERIAL PRIMARY KEY, created_at TIMESTAMPTZ, name TEXT, imagePath TEXT, type INTEGER);
    root@:26257/> CREATE TABLE  tracking.locationHistory (id SERIAL PRIMARY KEY, face_id INTEGER, created_at TIMESTAMPTZ, latitude DECIMAL(9,6), longitude DECIMAL(9,6), FOREIGN KEY (face_id) REFERENCES faceBank(id));
    root@:26257/> GRANT SELECT, INSERT, UPDATE ON tracking.faceBank TO maxroach;
    root@:26257/> GRANT SELECT, INSERT, UPDATE ON tracking.locationhistory TO maxroach;

### To run the API Server:

  ```bash
    > cd raspy && python ./src/Apiserver.py <local-ip> <port>
  ```

### To run the City Monitor Center (CMC):

  - Also exposes an API server in api-port

  ```bash
    > cd raspy && python ./src/cmc.py <local-ip> <port> <api-port>
  ```

### To run the Neighborhood Monitor Center (CMB):

  - Also exposes an API server in api-port

  ```bash
    > cd raspy && python ./src/cmb.py <local-ip> <port> <api-port> <cmc-ip> <cmc-port>
  ```

### To run the Web Server:

  ```bash
    > cd webapp/hawk-eye && npm start
  ```

### Before build the fedora env:

  You should:

  - Add the opencv-3.2.0 and opencv_contrib-3.2.0 folders to the raspy directory.
  To download the needed folders:

  ```bash
    > wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip
    > unzip opencv.zip
    > wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
    > unzip opencv_contrib.zip
  ```

  - Install docker.io:

  ```bash
    > apt-get install docker.io
  ```

### To build the fedora env:

  ```bash
    > ./docker-build.sh
  ```


### To run the env:

  ```bash
    > ./docker-start.sh
  ```

This will start the cmb.py script in background, and will let open a terminal.
