from django.contrib.gis.db import models


class CommonBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}.{1}".format(self.id, self.title)

    class Meta:
        abstract = True


class Municipality(CommonBaseModel):
    title = models.CharField(max_length=256)
    geometry = models.MultiPolygonField()
