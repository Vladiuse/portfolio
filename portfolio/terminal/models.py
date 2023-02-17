from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.files.storage import default_storage
import os
from django.template import Template, Context

# Create your models here.
class Directory(MPTTModel):
    DIR = 'dir'
    FILE = 'file'
    FILES_PATH = 'files'
    TYPES = (
        (DIR, DIR),
        (FILE, FILE)
    )

    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    type = models.CharField(max_length=5, blank=True, default=DIR, choices=TYPES)
    file_template = models.CharField(max_length=40, verbose_name='file_template', blank=True)


    def file_path(self):
        if self.type == self.FILE:
            return self.file_template
        else:
            return ''

    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        return self.name

    def get_content(self):
        file_path = os.path.join(self.FILES_PATH, str(self.file_template))
        text = default_storage.open(file_path).read()
        template = Template(str(text))
        context = Context({'user':'USER', 'x':'X VALUES'})
        content = template.render(context)
        return content



class Poll(models.Model):
    name = models.CharField(max_length=10, )

class Image(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')

