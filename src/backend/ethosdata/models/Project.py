from django.db import models

class Project(models.Model):
    """ A collection of clips related to a specific project. """
    STATUS_OPTIONS = [
        ('abandoned', 'Abandoned'),
        ('stuck', 'Stuck'),
        ('obsolete', 'Obsolete'),
        ('backlog', 'Backlog'),
        ('wip', 'Work In Progress'),
        ('completed', 'Completed'),
    ]

    REALM_OPTIONS = [
        ('end', 'The End'),
        ('ow', 'The Overworld'),
        ('nether', 'The Nether'),
    ]

    title = models.CharField(max_length=80, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS)

    # TODO: Figure out how to calculate these dates.
    first_updated = models.DateField()
    last_updated = models.DateField()

    # TODO: Figure out how to handle location data.
    x_location = models.DecimalField()
    y_location = models.DecimalField()
    z_location = models.DecimalField()
    realm_location = models.CharField(max_length=100, choices=REALM_OPTIONS)

    # TODO: Figure out how to add and remove clips/episodes/projects.
    clips = models.ManyToManyField()
    episodes = models.ManyToManyField()
    associated_projects = models.ManyToManyField()