# clab-radius
[Containerlab](https://containerlab.dev) topology built with freeRADIUS for testing with both Nokia SROS and SR Linux


## Deployment steps

### Prerequisites

- [ ] Containerlab [install link](https://containerlab.dev/install/)
- [ ] SROS license key [Discord](https://discord.gg/vAyddtaEV9)
- [ ] SROS container [containerlab](https://containerlab.dev/manual/kinds/vr-sros/)
- [ ] Docker [install link](https://docs.docker.com/engine/install/)

### freeRADIUS container

We must build the freeRADIUS container before deploying the topology. 

`docker build -t clab-radius -f Dockerfile .`

> Note: you can modify the freeRADIUS server settings before building the container by editing the files in `clab/raddb/`

You can verify the container has been built with `docker images | grep clab-radius`

### Start the topology

Now you can start the topology with the following command:

`cd clab; sudo clab deploy -t topo.yml --reconfigure`

> Note: you will need to have already acquired your license key for sros - make sure you have updated `topo.yml` with the correct location of the license file

Once the topology is fully booted, you will see the table with the details.

Here are the default users:

| User   | Password | Auth Type |
| :----- | :------: | :-------- |
| admin  | admin    | local     |
| drew   | admin    | radius    |

### freeRADIUS logs

To make it very easy to watch the logging for both the server and the accounting, I have the container logs sent to the host machine. *This also makes the logs persistent after destroying the lab*

The radius server log is at `clab/logs/radius.log`

The accounting log is at `clab/logs/radacct/<ip>` (192.168.6.2 is SRL and .3 is SROS)
> Note: you will need to use `sudo` to look at the accounting logs because of the sensitive nature of the contents