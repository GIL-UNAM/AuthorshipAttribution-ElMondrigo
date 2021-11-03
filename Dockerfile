FROM debian:11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    tzdata \
    ca-certificates \
    python3-venv\
    python3-pip \
    curl \
    && echo "America/Mexico_City" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && echo 'LANG="en_US.UTF-8"'>/etc/default/locale \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/share/zoneinfo/America/Mexico_City /etc/localtime

RUN curl https://download.java.net/openjdk/jdk17/ri/openjdk-17+35_linux-x64_bin.tar.gz | tar -xz -C /opt/

COPY ["requirements.txt", "/mondrigo/"]

WORKDIR /mondrigo

RUN pip3 install -r requirements.txt

COPY [".", "/mondrigo/"]

ENV JAVAHOME /opt/jdk-17/bin

CMD ["bash"]