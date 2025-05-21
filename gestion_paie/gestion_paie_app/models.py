from django.db import models

class Societe(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    num_cnss = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Employe(models.Model):
    SITUATION_FAMILIALE_CHOICES = [
        ('C', 'Célibataire'),
        ('M', 'Marié(e)'),
        ('D', 'Divorcé(e)'),
        ('V', 'Veuf(ve)'),
    ]

    CONTRAT_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('STAGE', 'Stage'),
    ]

    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    situation_familiale = models.CharField(max_length=1, choices=SITUATION_FAMILIALE_CHOICES)
    enfants = models.IntegerField(default=0)
    num_cnss = models.CharField(max_length=20)
    rib = models.CharField(max_length=24)
    date_embauche = models.DateField()
    type_contrat = models.CharField(max_length=5, choices=CONTRAT_CHOICES)
    qualification = models.CharField(max_length=100)
    salaire_base = models.DecimalField(max_digits=10, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.matricule})"

class BulletinPaie(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)
    mois = models.IntegerField()
    annee = models.IntegerField()
    jours_travailles = models.IntegerField()
    salaire_base = models.DecimalField(max_digits=10, decimal_places=3)
    prime_presence = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    indemnite_transport = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    prime_non_concurrence = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    cotisation_cnss = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    irpp = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    cotisation_solidarite = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    salaire_brut = models.DecimalField(max_digits=10, decimal_places=3)
    salaire_imposable = models.DecimalField(max_digits=10, decimal_places=3)
    salaire_net = models.DecimalField(max_digits=10, decimal_places=3)
    statut = models.CharField(max_length=10, choices=[('BROUILLON', 'Brouillon'), ('VALIDE', 'Validé'), ('PAYE', 'Payé')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employe', 'mois', 'annee')

    def __str__(self):
        return f"Bulletin {self.mois}/{self.annee} - {self.employe}"