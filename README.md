# clab-radius
[Containerlab](https://containerlab.dev) topology built with freeRADIUS for testing with both Nokia SROS and SR Linux


## Deployment steps

### Prerequisites

- [ ] Containerlab [install link](https://containerlab.dev/install/)
- [ ] Docker [install link](https://docs.docker.com/engine/install/)

### freeRADIUS container

We must build the freeRADIUS container before deploying the topology. 

`docker build -t clab-radius -f Dockerfile .`

> Note: you can modify the freeRADIUS server settings before building the container by editing the files in `clab/raddb/`

You can verify the container has been built with `docker images | grep clab-radius`

### Start the topology

Now you can start the topology with the following command:

`cd clab; sudo clab deploy -t topo.yml --reconfigure`

Once the topology is fully booted, you will see the table with the details.

Here are the default users:

| User   | Password | Auth Type |
| :----- | :------: | :-------- |
| admin  | admin    | local     |
| drew   | admin    | radius    |
