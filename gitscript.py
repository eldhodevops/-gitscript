#! /usr/bin/python
import os
import gitlab
import shutil
from multiprocessing.managers import public_methods

project_name = os.path.basename(os.getcwd())
print project_name

uname='xxxxx'
passwd='xxxxx'
group_id = 9
group_name = 'xxxxxx'

gl = gitlab.Gitlab('http://xxxxxxxxx', private_token=passwd)



# print os.walk(os.getcwd)
dir_list = next(os.walk('.'))[1]


for project_name in dir_list:
    print project_name
    os.chdir(project_name)
    project = gl.projects.create({'name': project_name, 'namespace_id': group_id, 'visibility': 'public'})
    hook = project.hooks.create({'url': 'http://xxxxxxx:88/hook/glpush', 'push_events': 1, 'enable_ssl_verification': False})
    
    returned_value = os.system("git --version")  # returns the exit code in unix
    print('returned value:', returned_value)
    dot_git = './.git'
    if os.path.isdir(dot_git):
        shutil.rmtree(dot_git)
        
    
    url = 'http://'+uname+':'+passwd+'@xxxxxx'+project_name+'.git'
    
    os.system("git init")
    os.system('git remote add origin http://'+uname+':'+passwd+'@xxxxx/'+group_name+'/'+project_name+'.git')
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")
    os.system("git push -u origin master")
    os.chdir("../")
#     quit()
