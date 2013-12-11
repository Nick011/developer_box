from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter
from django.db import models
from django.contrib.auth.models import User
from tag import Tag

class Item(models.Model):
	user = models.ForeignKey(User)
	tag = models.ManyToManyField(Tag)
	title = models.CharField(max_length=75, blank=False, null=False)
	body = models.TextField(blank=False, null=False)
	script = models.TextField(blank=False, null=False)
	slug = models.SlugField(unique=True, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
	last_viewed_at = models.DateTimeField(auto_now=True, auto_now_add=True)

	class Meta:
		app_label = "developer_box"

	def highlight_script(self):
		lexer = guess_lexer(self.script, stripall=True)
		formatter = HtmlFormatter(linenos=True, cssclass="source")
		return highlight(self.script, lexer, formatter)

	def __unicode__(self):
		return self.title
