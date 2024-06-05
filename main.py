from datetime import datetime
from typing import List


""" la classe membre representant une personne """


class Membre:
    def __init__(self, nom: str, role: str):
        self.nom = nom
        self.role = role


""" la classe equipe qui est composée de zéro ou plusieurs membres"""


class Equipe:
    def __init__(self):
        """Initialise une nouvelle équipe avec une liste vide de membres."""
        self.membres = []

    def ajouter_membre(self, membre: Membre):
        """Ajoute un membre à l'équipe."""
        self.membres.append(membre)

    def obtenir_membres(self):
        """Retourne la liste des membres de l'équipe."""
        return self.membres


class Tache:
    """Représente une tâche avec ses attributs et ses méthodes."""

    def __init__(
        self,
        nom: str,
        description: str,
        date_debut: datetime,
        date_fin: datetime,
        responsable: Membre,
        statut: str,
    ):
        """Initialise une nouvelle tâche."""

        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances: List = []

    def ajouter_dependance(self, tache: "Tache"):
        """Ajoute une dépendance à la tâche."""
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str):
        """Met à jour le statut de la tâche."""
        self.statut = statut


"""Représente un jalon dans un projet avec un nom et une date."""


class Jalon:
    def __init__(self, nom: str, date: datetime):
        """Initialise un nouveau jalon."""
        self.nom = nom
        self.date = date


"""Représente un risque potentiel dans un projet avec
une description, une probabilité et un impact."""


class Risque:
    def __init__(self, description: str, probabilite: float, impact: str):
        """Initialise un nouveau risque."""
        self.description = description
        self.probabilite = probabilite
        self.impact = impact


"""Représente un changement dans un projet avec """
"""une description, une version et une date."""


class Changement:
    def __init__(self, description: str, version: int, date: datetime):
        """Initialise un nouveau changement."""
        self.description = description
        self.version = version
        self.date = date


"""Classe de base pour les stratégies de notification."""


class NotificationStrategy:
    def envoyer(self, message: str, destinataire: Membre):
        """Envoie une notification à un destinataire."""
        pass


"""Stratégie de notification par email."""


class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre):
        """Envoie une notification par email à un destinataire."""
        print(f"Notification envoyée à " f"" f"{destinataire.nom} par email: {message}")


"""Stratégie de notification par SMS."""


class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre):
        """Envoie une notification par sms à un destinataire."""
        print(f"Notification envoyée à" f" " f"{destinataire.nom} par SMS: {message}")


class PushNotificationStrategy(NotificationStrategy):
    """envoie une notification push au destinataire"""

    def envoyer(self, message: str, destinataire: Membre):
        print(f"Notification envoyée à {destinataire.nom} : {message}")


class NotificationContext:
    def __init__(self, strategy: NotificationStrategy):
        """Initialise le contexte de notification avec"""
        """une stratégie spécifique"""
        self.strategy = strategy

    def notifier(self, message: str, destinataires: List[Membre]):
        """Notifie tous les destinataires en"""
        """utilisant la stratégie de notification spécifiée"""
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)


class Projet:
    def __init__(
        self, nom: str, description: str, date_debut: datetime, date_fin: datetime
    ):
        """Initialise les attributs du projet"""
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches: List = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques: List = []
        self.jalons: List = []
        self.version = 1
        self.changements: List = []
        self.chemin_critique: List = []
        self.notification_context: NotificationContext = NotificationContext(
            EmailNotificationStrategy()
        )

    def set_notification_strategy(self, strategy: NotificationStrategy):
        """Définit la stratégie de notification pour le projet"""
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache):
        """Ajoute une nouvelle tâche au projet et notifie l'équipe"""
        self.taches.append(tache)
        self.notifier(
            f"Nouvelle tâche ajoutée:" f" {tache.nom}", self.equipe.obtenir_membres()
        )

    def ajouter_membre_equipe(self, membre: Membre):
        """Ajoute un nouveau membre à l'équipe du projet et"""
        """envoie une notification"""
        self.equipe.ajouter_membre(membre)
        self.notifier(f"{membre.nom} a été ajouté à l'équipe", [membre])

    def definir_budget(self, budget: float):
        """Définit le budget du projet et notifie l'équipe"""
        self.budget = budget
        self.notifier(
            f"Le budget du projet a été défini à {budget} Unité Monetaire",
            self.equipe.obtenir_membres(),
        )

    def ajouter_risque(self, risque: Risque):
        """Ajoute un nouveau risque au projet et notifie l'équipe"""
        self.risques.append(risque)
        self.notifier(
            f"Nouveau risque ajouté: {risque.description}",
            self.equipe.obtenir_membres(),
        )

    def ajouter_jalon(self, jalon: Jalon):
        """Ajoute un nouveau jalon au projet et notifie l'équipe"""
        self.jalons.append(jalon)
        self.notifier(
            f"Nouveau jalon ajouté: {jalon.nom}", self.equipe.obtenir_membres()
        )

    def enregistrer_changement(self, description: str):
        """Enregistre un nouveau changement dans le"""
        """projet et notifie l'équipe"""
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)
        self.notifier(
            f"Changement enregistré: {description} (version {self.version})",
            self.equipe.obtenir_membres(),
        )
        self.version += 1

    def notifier(self, message: str, destinataires: List[Membre]):
        """Notifie les membres de l'équipe en utilisant le"""
        """contexte de notification"""
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)

    def generer_rapport_performance(self):
        """Génère un rapport de performance du projet"""
        get_membres = "\n".join(
            [
                f"- {membre.nom} ({membre.role})"
                for membre in self.equipe.obtenir_membres()
            ]
        )
        get_taches = "\n".join(
            [
                f"- {tache.nom} ({tache.date_debut} a {tache.date_fin}), "
                f"Responsable: {tache.responsable.nom}, Statut: {tache.statut}"
                for tache in self.taches
            ]
        )
        get_jalons = "\n".join(
            [f"- {jalon.nom} ({jalon.date})" for jalon in self.jalons]
        )
        get_risques = "\n".join(
            [
                f"- {risque.description} (Probabilité: {risque.probabilite}, "
                f"Impact: {risque.impact})"
                for risque in self.risques
            ]
        )
        get_chemin_critiques = "\n".join(
            [
                f"- {tache.nom} ({tache.date_debut} a {tache.date_fin})"
                for tache in self.taches
            ]
        )

        return (
            "#################################################\n"
            f"Rapport de performance du projet {self.nom}\n"
            f"Version : {self.version}\n"
            f"Dates : {self.date_debut} à {self.date_fin}\n"
            f"Budget : {self.budget} FCFA\n"
            f"Équipe :\n{get_membres}\n"
            f"Taches :\n{get_taches}\n"
            f"jalons :\n{get_jalons}\n"
            f"Risques :\n{get_risques}\n"
            f"Chemin Critiques :\n{get_chemin_critiques}"
        )

    def calculer_chemin_critique(self):
        """calculer le chemin critique"""
        return self.chemin_critique


if __name__ == "__main__":
    projet = Projet(
        "Nouveau Produit",
        "Développement d'un nouveau produit",
        datetime(2024, 1, 1),
        datetime(2024, 12, 31),
    )
    projet2 = Projet(
        "Gestion pfc",
        "Gestion",
        datetime(2024, 1, 1),
        datetime(2024, 12, 31),
    )
    projet2.calculer_chemin_critique()
    membre1 = Membre("Latyr omar", "Chef de projet")
    membre2 = Membre("Mamy watta", "Développeur")

    projet.ajouter_membre_equipe(membre1)
    projet.ajouter_membre_equipe(membre2)

    tache1 = Tache(
        "Analyse des besoins",
        "Description de la tâche",
        datetime(2024, 1, 1),
        datetime(2024, 1, 31),
        membre1,
        "Terminée",
    )
    tache2 = Tache(
        "Développement",
        "Description de la tâche",
        datetime(2024, 2, 1),
        datetime(2024, 6, 30),
        membre2,
        "Non démarrée",
    )

    projet.ajouter_tache(tache1)
    projet.ajouter_tache(tache2)

    tache1.ajouter_dependance(tache2)
    tache1.mettre_a_jour_statut("arret")

    projet.definir_budget(50000)

    risque1 = Risque("Retard de livraison", 0.3, "Élevé")
    projet.ajouter_risque(risque1)

    jalon1 = Jalon("Phase 1 terminée", datetime(2024, 1, 31))
    projet.ajouter_jalon(jalon1)

    projet.set_notification_strategy(EmailNotificationStrategy())
    projet.set_notification_strategy(SMSNotificationStrategy())
    projet2.set_notification_strategy(PushNotificationStrategy())

    projet.enregistrer_changement("Changement de la portée du projet")
    print(projet.generer_rapport_performance())
