FROM docker.io/oraclelinux:7
 
# Install hotwrap binary in the container
COPY --from=fnproject/hotwrap:latest  /hotwrap /hotwrap
 
# Function runs by fn user (uid 1000), it has to be created
# RUN commit changes into new image during build time
RUN groupadd --gid 1000 fn && \
     adduser --uid 1000 --gid fn -d /home/fn fn && \
     mkdir -p /home/fn/.ssh && chown -R fn:fn /home/fn/.ssh && chmod 700 /home/fn/.ssh
COPY id_rsa-opc /home/fn/.ssh/id_rsa-opc
RUN chown fn:fn /home/fn/.ssh/id_rsa-opc && chmod 400 /home/fn/.ssh/id_rsa-opc
COPY ldap_config.sh /ldap_config.sh
 
# hard-coded OCI compute name
ENV COMPUTE <oci-compute-name>
RUN echo $COMPUTE > /compute.txt
 
# CMD defines argument for ENTRYPOINT
CMD "/bin/scp -i /home/fn/.ssh/id_rsa-opc -o \"StrictHostKeyChecking no\" /ldap_config.sh opc@`echo $COMPUTE`:/tmp && /bin/ssh -i /home/fn/.ssh/id_rsa-opc -o \"StrictHostKeyChecking no\" opc@`echo $COMPUTE` \"sudo /tmp/ldap_config.sh\" "
# Defines what to executes during container runtime
ENTRYPOINT ["/hotwrap"]

