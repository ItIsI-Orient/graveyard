# This module contains models that are acutally used in the current state
# of the application
# It still represents a "transitional" state needed to cooperate with
# the old application; hence do not grin at missing ForeignKeys and similar
# "rooms for improvement" that can be done once the original application
# is strangled out of its existence

import re
from unicodedata import normalize, combining

from django.db import models
from django.contrib.auth.models import User

from ..magic import MisencodedCharField, MisencodedTextField, MisencodedIntegerField
from ...commonarticles import COMMON_ARTICLES_CREATIVE_PAGES

APPROVAL_CHOICES = (
    ('a', 'Schváleno'),
    ('n', 'Neschváleno'),
)

###
# Introduce an umbrella model for all Creations
###

class CreativePage(models.Model):
    """ I represent a Creative Page as a first-item concept to help with foreign keys, definitions etc. """
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    editors = models.ManyToManyField(User)

class CreativePageSection(models.Model):
    """ Section within a Creative Page """
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

class CreativePageConcept(models.Model):
    page = models.OneToOneField(CreativePage, on_delete=models.CASCADE)
    text = models.TextField()
    
class Creation(models.Model):
    """
    Encapsulates common fields and actions for all creations. Please note:

        * This is introduced as a new concept in the rewrite, hence
            backward-compatible handling of all relations is needed
        * It may be tempting to add "popis" or "anotace" to the model, but
            note that (Photo)Gallery is part of this as well
        * Authors are _not_ handled using ForeignKeys -- this is to be introduced later
        * `pochvez` (aka rating) CAN'T be recomputed from CreationVotes since votes are not created equal:
            - Editor's vote is counted as three votes
            - The Head of a Gold Dragon Awards flatly marks winners as having six stars

            Neither of those is tracked in database very well and such information is lost.
            Be careful, don't lose aggregates!
    """
    jmeno = MisencodedTextField()
    autor = MisencodedCharField(max_length=25, blank=True, null=True)
    autmail = MisencodedCharField(max_length=30, blank=True, null=True)
    schvaleno = MisencodedCharField(max_length=1, choices=APPROVAL_CHOICES)
    zdroj = MisencodedTextField(blank=True, null=True)
    zdrojmail = MisencodedCharField(max_length=30, blank=True, null=True)
    pocet_hlasujicich = models.IntegerField(blank=True, null=True)
    hodnota_hlasovani = models.IntegerField(blank=True, null=True)
    pochvez = MisencodedIntegerField(max_length=5)
    precteno = models.IntegerField(default=0)
    tisknuto = models.IntegerField(default=0)
    datum = models.DateTimeField(auto_now_add=True)

    # section = models.ForeignKey(CreativePageSection, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

    def get_slug(self):
        # slug = normalize('NKFD', self.jmeno)
        slug = normalize('NFD', self.jmeno)
        slug = ''.join([ch for ch in slug if not combining(ch)]).lower()
        slug = re.sub("[^a-z0-9]+", "-", slug)
        slug = re.sub("^([^a-z0-9])+", "", slug)
        slug = re.sub("([^a-z0-9]+)$", "", slug)
        return slug

###
# Handle all models that should work with all creations.
# Do note that for backward compatibility, all relations to creations
# has to be NULLable and that (lazy) migration is needed in order to fix
# this model
###


class CreationVotes(models.Model):
    # creation = models.OneToMany(Creation) -- to be introduced later
    #TODO: Would conversion to ForeignKey work..and would it work to User?
    id_uz = models.IntegerField(primary_key=True)
    id_cizi = models.IntegerField()
    rubrika = models.CharField(max_length=20)
    pochvez = models.IntegerField()
    time = models.IntegerField()
    opraveno = models.CharField(max_length=1)

    class Meta:
        db_table = 'hlasovani_prispevky'
        unique_together = (('id_uz', 'id_cizi', 'rubrika'),)


###
# Particular models for all creations follow
###

class CommonArticles(Creation):
    text = MisencodedTextField()
    skupina = MisencodedCharField(max_length=30, blank=True, null=True)
    anotace = MisencodedTextField(blank=True, null=True)
    rubrika = MisencodedCharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'prispevky_dlouhe'
        verbose_name = 'Běžné příspěvky'
        verbose_name_plural = 'Běžné příspěvky'

    def __str__(self):
        return "{}: {} od {}".format(
            # COMMON_ARTICLES_CREATIVE_PAGES[self.rubrika]['name'],
            self.rubrika,
            self.jmeno,
            self.autor,
        )


class Monster(Creation):
    zvt = models.TextField()
    uc = models.TextField()
    oc = models.TextField()
    odl = models.CharField(max_length=3)
    inteligence = models.CharField(max_length=50, blank=True, null=True)
    vel = models.CharField(max_length=20)
    zran = models.TextField(blank=True, null=True)
    poh = models.TextField(blank=True, null=True)
    pres = models.TextField(blank=True, null=True)
    pokl = models.TextField(blank=True, null=True)
    zkus = models.CharField(max_length=50)
    popis = models.TextField()
    skupina = models.TextField()
    bojovnost = models.CharField(max_length=50, blank=True, null=True)
    sm = models.CharField(db_column='SM', max_length=50)  # Field name made lowercase.
    tisknuto = models.PositiveIntegerField()

    class Meta:
        db_table = 'bestiar'
