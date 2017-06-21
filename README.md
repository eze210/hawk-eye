# hawk-eye
Distributed system to track objects or faces from images.


### Before build the fedora env:

  You should add the opencv-3.2.0 and opencv_contrib-3.2.0 folders to the raspy directory.
  To download the needed folders:

  ```bash
    > wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip
	> unzip opencv.zip
	> wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
	> unzip opencv_contrib.zip
  ```


### To build the fedora env:

  ```bash
    > ./docker-build.sh
  ```


### To run the env:

  ```bash
    > ./docker-start.sh
  ```

This will start the server.py script in background, and will let open a terminal.
