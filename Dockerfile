FROM debian

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    python-pip \
    python-tk \
    vim

WORKDIR /root
RUN curl -L http://download.osgeo.org/libspatialindex/spatialindex-src-1.8.5.tar.gz | tar xz
WORKDIR spatialindex-src-1.8.5
RUN ./configure
RUN make
RUN make install
RUN ldconfig

WORKDIR /root/src
RUN pip install osmnx
ADD main.py .
CMD python main.py