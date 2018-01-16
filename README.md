# Logs Analysis
An application that uses information from the PostgreSQL database to report:
* What are the most popular three articles of all time;
* Who are the most popular article authors of all time;
* On which days did more than 1% of requests lead to errors.

## Running with Virtual Machine
### Prerequisites
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Install [Vagrant](https://www.vagrantup.com/)

### Installation
* Download Vagrant VM
`git clone https://github.com/udacity/fullstack-nanodegree-vm.git`
* In terminal, change current directory to vagrant
`cd <your_path>/fullstack-nanodegree-vm/vagrant`
* Download project into vagrant
`git clone https://github.com/msurmenok/logs-analysis.git`

### Start Virtual Machine
* In terminal (in vagrant folder) launch virtual machine `vagrant up`
(The first launch requires some time to install all dependencies)
* Connect to vm `vagrant ssh`
* Return to project folder `cd /vagrant/logs-analysis`
### Download the Data
* Use [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to download the data and unzip to the project directory.
* Load the data to PostreSQL typing in terminal `psql -d news -f newsdata.sql`
### Run the Project
Run file `python application.py`