from .models import BulletinPaie

def calculer_paie(employe, mois, annee):
    # Paramètres
    taux_cnss_employe = 0.0918
    taux_irpp_tranches = [
        {'min': 0, 'max': 5000, 'taux': 0.0, 'deduction': 0},
        {'min': 5001, 'max': 20000, 'taux': 0.26, 'deduction': 1300},
        {'min': 20001, 'max': 30000, 'taux': 0.28, 'deduction': 1900},
        {'min': 30001, 'max': 50000, 'taux': 0.32, 'deduction': 3100},
        {'min': 50001, 'taux': 0.35, 'deduction': 4600},
    ]
    taux_solidarite = 0.01

    # Calculs
    jours_travailles = 26
    salaire_base = (float(employe.salaire_base) / 30) * jours_travailles

    prime_presence = 7.080
    indemnite_transport = 36.112
    prime_non_concurrence = 608.743

    salaire_brut = salaire_base + prime_presence + indemnite_transport + prime_non_concurrence

    cotisation_cnss = salaire_brut * taux_cnss_employe
    salaire_imposable = salaire_brut - cotisation_cnss

    irpp = 0
    for tranche in taux_irpp_tranches:
        min_tranche = tranche['min']
        max_tranche = tranche.get('max', float('inf'))
        if salaire_imposable > min_tranche:
            base = min(salaire_imposable, max_tranche) - min_tranche
            irpp += base * tranche['taux'] - tranche['deduction']

    cotisation_solidarite = salaire_imposable * taux_solidarite
    salaire_net = salaire_imposable - irpp - cotisation_solidarite

    # Création du bulletin
    bulletin = BulletinPaie.objects.create(
        employe=employe,
        societe=employe.societe,
        mois=mois,
        annee=annee,
        jours_travailles=jours_travailles,
        salaire_base=salaire_base,
        prime_presence=prime_presence,
        indemnite_transport=indemnite_transport,
        prime_non_concurrence=prime_non_concurrence,
        cotisation_cnss=cotisation_cnss,
        irpp=irpp,
        cotisation_solidarite=cotisation_solidarite,
        salaire_brut=salaire_brut,
        salaire_imposable=salaire_imposable,
        salaire_net=salaire_net,
        statut='BROUILLON'
    )
    return bulletin