FROM centos:7.2.1511

# install systemd
ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]

# example - httpd
#RUN yum -y install httpd; yum clean all; systemctl enable httpd.service
#EXPOSE 80

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# install pip
# install gcc and python-devel
RUN yum -y install epel-release-7-9.noarch && yum -y install python2-pip-8.1.2-5.el7.noarch && \
    yum -y group install "Development Tools" && yum -y install python-devel && yum clean all

# copy apisvc release
COPY data/requirements.txt /vagrant/data/requirements.txt

# install apisvc dependency
# NOTE '; yum clean all' is a workaround to fix 'Rpmdb checksum is invalid: dCDPT(pkg checksums)'
RUN pip install -r /vagrant/data/requirements.txt && \
    yum -y install jq-1.5-1.el7.x86_64 openssl-1:1.0.2k-8.el7.x86_64 coreutils-8.22-18.el7-x86_64; yum clean all && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.8.0/bin/linux/amd64/kubectl && chmod +x kubectl && mv kubectl /usr/bin

# copy apisvc release
COPY data/* /vagrant/data/*

# install apisvc
# install apisvc systemd service unit
RUN pip install /vagrant/data/apisvc-1.0.0.tar.gz && \
    cp /vagrant/data/apisvc.service /usr/lib/systemd/system/ && chmod 664 /usr/lib/systemd/system/apisvc.service && systemctl enable apisvc

# expose apisvc
EXPOSE 5080

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

CMD ["/usr/sbin/init"]
