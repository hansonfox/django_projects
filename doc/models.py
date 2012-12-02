from django.db import models

class Doc(models.Model):
    name = models.CharField(max_length=10)
    reunit = models.CharField(max_length=20)
    doc_num = models.CharField(max_length=10)
    in_date = models.DateField()


    def __unicode__(self):
        return '%s %s %s' % (self.name,self.reunit,self.doc_num)

    class Meta:
        ordering = ['-in_date']
        verbose_name = 'documents'

    #def save():


class Record(models.Model):
    REC_TYPE = (
        ('IN','IN'),
        ('OUT'，'OUT'),
        ('')
        )    
