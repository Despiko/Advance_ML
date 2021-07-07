Comand to build:
docker build -t myimage \
  --build-arg USER_ID=$(id -u) \
  --build-arg GROUP_ID=$(id -g) .
  
  
Command to run container:
 docker run -it --rm \
-v $(pwd)/star_vol:/starspace/star_vol myimage


You need to have file text.txt in star_vol folder.
When you run container this file will preprocess.
