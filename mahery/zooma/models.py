from django.db import models

# Create your models here.


class Versement(models.Model):
     banque = models.CharField(max_length=50)

class Creance(models.Model):
    id = models.IntegerField( primary_key=True)

class Billetage(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField

class Type(models.Model):
    TYPE_PAYEMENT = (
        ('E', 'Espece'),
        ('V', 'Visa'),
        ('B', 'Banque'),
        ('M', 'MobileMoney'),
    )
    name = models.CharField(max_length=60)
    type_payement = models.CharField(max_length=1, choices=TYPE_PAYEMENT)

class Payement(Type):
    type = models.CharField(max_length=11)


class Client(models.Model):
    nom = models.CharField(max_length=50)
    premon = models.CharField(max_length=50)

class PointDeVente(models.Model):
    id = models.IntegerField(primary_key=True)
    nom_service = models.CharField(max_length=11)

class Service(models.Model):
    SERVICE= (
        ('H', 'Hebergement'),
        ('S', 'Snack'),
        ('R', 'Resto'),
        ('A', 'ApproSahalava'),
    )
    name = models.CharField(max_length=60)
    service = models.CharField(max_length=1, choices=SERVICE)
    point_de_vente = models.IntegerField(11, primary_key=True)
    prelevement = models.IntegerField(11, primary_key=True)

class CientHasChambre(models.Model):
    client_id  = models.IntegerField(11, primary_key=True)
    client_payement_id = models.IntegerField(11, primary_key=True)
    client_service_id = models.IntegerField(11, primary_key=True)
    chambre_id = models.IntegerField(11, primary_key=True)

class Chambre(models.Model):
    chambre_id = models.IntegerField(11, primary_key=True)
    type_chambre = models.CharField(max_length=50)
    numero_Chambre = models.IntegerField(56)
    Occupation = models.BooleanField

class Prelevement(models.Model):
    id_client = models.IntegerField(11)

class Approvisionement(models.Model):
    economat_id = models.IntegerField(11, primary_key=True)
    fournisseur_id = models.IntegerField(11, primary_key=True)

class Economat(models.Model):
    id = models.IntegerField(11, primary_key=True)
    prelevement_id = models.ForeignKey(Prelevement, on_delete=CASCADE)
    stock = models.IntegerField(11, primary_key=True

cla










