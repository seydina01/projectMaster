from datetime import datetime

#la classe membre representant une  personne
class Membre:
    def __init__(self, nom: str, role: str):
        self.nom = nom
        self.role = role

#la classe equipe qui est composée de zéro ou plusieurs membres
class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre: Membre):
        self.membres.append(membre)

    def obtenir_membres(self):
        return self.membres

class Tache:
    def __init__(self, nom: str, description: str, date_debut: datetime, date_fin: datetime, responsable: Membre, statut: str):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances = []

    def ajouter_dependance(self, tache: 'Tache'):
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str):
        self.statut = statut

class Jalon:
    def __init__(self, nom: str, date: datetime):
        self.nom = nom
        self.date = date

class Risque:
    def __init__(self, description: str, probabilite: float, impact: str):
        self.description = description
        self.probabilite = probabilite
        self.impact = impact

class Changement:
    def __init__(self, description: str, version: int, date: datetime):
        self.description = description
        self.version = version
        self.date = date

class Projet:
    def __init__(self, nom: str, description: str, date_debut: datetime, date_fin: datetime):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques = []
        self.jalons = []
        self.version = 1
        self.changements = []
        self.chemin_critique = []
        self.notification_context = None

    def ajouter_tache(self, tache: Tache):
        self.taches.append(tache)
        self.notifier(f"Nouvelle tâche ajoutée: {tache.nom}", self.equipe.obtenir_membres())

    def ajouter_membre_equipe(self, membre: Membre):
        self.equipe.ajouter_membre(membre)
        self.notifier(f"{membre.nom} a été ajouté à l'équipe", [membre])

    def definir_budget(self, budget: float):
        self.budget = budget
        self.notifier(f"Le budget du projet a été défini à {budget} Unité Monetaire", self.equipe.obtenir_membres())

    def ajouter_risque(self, risque: Risque):
        self.risques.append(risque)
        self.notifier(f"Nouveau risque ajouté: {risque.description}", self.equipe.obtenir_membres())

    def ajouter_jalon(self, jalon: Jalon):
        self.jalons.append(jalon)
        self.notifier(f"Nouveau jalon ajouté: {jalon.nom}", self.equipe.obtenir_membres())

    def enregistrer_changement(self, description: str):
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)
        self.notifier(f"Changement enregistré: {description} (version {self.version})", self.equipe.obtenir_membres())
        self.version += 1

    def notifier(self, message: str, destinataires: [Membre]):
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)

    def generer_rapport_performance(self):
        get_membres = "\n".join([f"- {membre.nom} ({membre.role})" for membre in self.equipe.obtenir_membres()])

        return (
            f"Rapport de performance du projet {self.nom}\n"
            f"Version : {self.version}\n"
            f"Dates : {self.date_debut} à {self.date_fin}\n"
            f"Budget : {self.budget} FCFA\n"
            f"Équipe :\n{get_membres}"
        )

    def calculer_chemin_critique(self):
        pass

if __name__ == "__main__":
    membre1 = Membre("seydina Diagne", "Développeur")
    membre2 = Membre("latyr Diedhiou", "Manager")

    membre3 = Membre("Mamadou Ba", "Développeur")
    membre4 = Membre("Ameth Gaye", "Manager")

    projet1 = Projet("Gestion des vacataires", "projet visant  a faciliter la gestion des vacataires au sein de l'UFR SET", '2024-05-01', '2024-06-01')
    projet2 = Projet("Gestion des PFC", "projet visant  a faciliter la gestion des projetsde fin de cycle", '2024-05-01', '2024-06-01')

    projet1.ajouter_membre_equipe(membre3)
    projet1.ajouter_membre_equipe(membre4)
    print(projet1.generer_rapport_performance())

