import re
from django import template
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def as_template(form):
  template = get_template("forms/form.html")
  c = Context({"form": form})
  return template.render(c)


@register.filter
def css_class(field):
  return field.field.widget.__class__.__name__.lower()


class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')
@register.filter
def add_class(value, css_class):
  string = unicode(value)
  match = class_re.search(string)
  if match:
    m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class, 
                                                css_class, css_class), 
                                                match.group(1))
    if not m:
      return mark_safe(class_re.sub(match.group(1) + " " + css_class, 
                                      string))
  else:
    return mark_safe(string.replace('>', ' class="%s">' % css_class))
  return value


@register.filter
def error_class(errors):
  if errors: return 'has-error'
