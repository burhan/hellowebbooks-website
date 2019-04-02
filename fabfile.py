import getpass
import os
from fabric import task, Connection, Config


@task
def deploy(c):
    sudo_pass = os.environ.get('SUDO_PW')
    if not sudo_pass:
        sudo_pass = getpass.getpass("sudo password? (or set $SUDO_PW): ")
    
    server_address = os.environ.get('SERVER_ADDRESS')
    if not server_address:
        server_address = input("server address? (or set $SERVER_ADDRESS): ")

    config = Config(overrides={'sudo': {'password': sudo_pass}})
    c = Connection(host=server_address, user=os.environ['POSTGRES_US'], config=config)
    with c.cd('hellowebbooks/hellowebbooks'):
        c.run('git pull origin master')

    c.sudo('systemctl restart gunicorn')
    c.sudo('journalctl -u gunicorn --since "1 min ago"')
