FROM quay.io/pypa/manylinux2014_aarch64 AS manylinux

FROM rustembedded/cross:aarch64-unknown-linux-gnu

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa \
RUN apt-get update
RUN apt-get install -y python3.9

COPY --from=manylinux /opt/_internal /opt/_internal
COPY --from=manylinux /opt/python /opt/python