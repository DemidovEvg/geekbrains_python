from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import FunctionLoader

file_loader = FileSystemLoader('work/templates')
env = Environment(loader=file_loader)

subs = ['first', 'second', 'third']


tm = env.get_template('child.htm')
msg = tm.render(list_table=subs)

print(msg)