import yaml

conf = yaml.load(open('conf/application.yml'), Loader=yaml.FullLoader)
engine = conf['db']['engine']
server = conf['db']['server']
database = conf['db']['database']
username = conf['db']['username']
password = conf['db']['password']

print (engine)