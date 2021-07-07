FROM ubuntu:18.04

WORKDIR /starspace

COPY requirements.txt requirements.txt

RUN \
	apt-get update && apt-get install -y \
	autoconf \
    automake \
	libtool \
	build-essential \
	unzip \
	git \
	wget \
	python3\
	python3-pip -y


RUN pip3 install -r requirements.txt


RUN \
    wget https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz && \
    tar -xf boost_1_63_0.tar.gz && \
    mv boost_1_63_0 /usr/local/bin


RUN \
	git clone https://github.com/facebookresearch/Starspace.git && \
	cd Starspace && \
	make && \
	make embed_doc && \
	make query_nn && \
	make print_ngrams && \
	make query_predict



ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user

RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

USER user

CMD \
    cd /starspace/star_vol && \
    python3 preprocess.py && \
     cd /starspace/Starspace && \
     ./starspace train -trainFile /starspace/star_vol/train_starspace.txt \
     -model /starspace/star_vol/modelSaveFile

