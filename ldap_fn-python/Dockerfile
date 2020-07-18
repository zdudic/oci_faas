FROM oraclelinux:8
 
RUN groupadd --gid 1000 fn && \
    adduser --uid 1000 --gid fn -d /home/fn fn && \
    mkdir -p /home/fn/.ssh && chown -R fn:fn /home/fn/.ssh && chmod 700 /home/fn/.ssh
 
WORKDIR /function
ADD requirements.txt /function/
ADD id_rsa-opc /home/fn/.ssh
 
RUN yum -y install python36 && pip3 install --no-cache --no-cache-dir -r requirements.txt && \
     rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv && \
     chown fn:fn /home/fn/.ssh/id_rsa-opc && chmod 400 /home/fn/.ssh/id_rsa-opc
 
ADD . /function/
RUN rm -fr /function/.pip_cache
 
ENTRYPOINT ["/usr/local/bin/fdk", "/function/func.py", "handler"]
