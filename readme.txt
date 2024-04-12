- login to virtual machine using ssh
ssh -i [path_to_ssh_key] liush@[external_ip]

-install virtualenv
sudo apt update
sudo apt install virtualenv

- download software
git clone https://github.com/shul159/cyberattack_flask.git

- activate virtual environment
virtualenv --python=python3 cyberattack
source cyberattack/bin/activate

- run application with nohup
nohup python app.py > out &
- if we want to shut down the app, run
kill [process number]
process number can be obtained by command: ps aux

-(optional) upload from local:
scp test.model [xxx@ip_address]:[destination_path]

-(optional) upload directory
scp -r test.model [xxx@ip_address]:[destination_path]

- publish app
in GCP, vm instances->... -> view network details-> fire wall->create firewall rule->name flask, source ipv4 ranges 0.0.0.0/0, tcp: 5000
in browser [external ip]:5000
exampe http://34.125.102.165:5000/
