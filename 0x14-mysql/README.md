mysql primary replica setup

```bash
#sql installation steps
sudo apt update
wget https://repo.mysql.com//mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

sudo apt update

wget -qO - https://repo.mysql.com/RPM-GPG-KEY-mysql-2023 | sudo apt-key add -wget -qO - https://repo.mysql.com/RPM-GPG-KEY-mysql-2023 | sudo apt-key add -
sudo apt install mysql-client=5.7.*-1ubuntu18.04
sudo apt install mysql-community-server=5.7.*-1ubuntu18.04 # prompts for root password
sudo apt install mysql-server=5.7.*-1ubuntu18.04
```
