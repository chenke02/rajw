# -*- coding: utf-8 -*-
# author:chenke

import os
cmd = 'cd E:\Web\Python\Django1'
os.system(cmd)
cmd1 = 'cd E:'
os.system(cmd1)
cmd = 'python manage.py makemigrations learn'
os.system(cmd)
cmd2 = 'python manage.py migrate learn'
os.system(cmd2)
