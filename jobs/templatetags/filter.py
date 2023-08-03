from django import template

register = template.Library()

def split(value, arg):
    return value.split(arg)
register.filter('split', split)

def replace(value):
    return value.replace("[", "").replace("]","",).replace(",","").replace("'","")
register.filter("replace", replace)

def remove(value, args):
    return value.replace(args, "")
register.filter('remove',remove)

def remove_sym(value):
    if '[' in value:
        value= value.replace("[", "")
    if ']' in value:
        value= value.replace("]", "")
    if '"' in value:
        value= value.replace('"', '')
    if "'" in value:
        value= value.replace("'", "")
    return value
register.filter('remove_sym',remove_sym)