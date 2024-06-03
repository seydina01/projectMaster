import unittest
from main import (
    Equipe,
    Membre,
    Tache,
    Jalon,
    Risque,
    Projet
)

class TestProjectManager(unittest.TestCase):
    def setUp(self):
        self.membre1 = Membre("Mamie Awa WATT", "Développeuse")
        self.membre2 = Membre("Mouhamed Gaye", "Manager")
        self.membre3 = Membre("Seydina Issa Diagne", "Développeur")
        self.membre4 = Membre("Latyr Omar Diedhiou", "Manager")

        self.equipe = Equipe()
        self.equipe.ajouter_membre(self.membre1)
        self.equipe.ajouter_membre(self.membre2)
        self.equipe.ajouter_membre(self.membre3)
        self.equipe.ajouter_membre(self.membre4)

        self.tache1 = Tache("Analyse des besoins", "Analyse des besoins du projet", '2024-05-01', '2024-05-09', self.membre3, "Terminé")
        self.tache2 = Tache("Développement", "Analyse DevOps", '2024-06-01', '2024-06-01', self.membre4, "En cours")

        self.projet1 = Projet("Gestion des vacataires", "Projet visant à faciliter la gestion des vacataires au sein de l'UFR SET", '2024-05-01', '2024-06-01')
        self.projet2 = Projet("Gestion des PFC", "Projet visant à faciliter la gestion des projets de fin de cycle", '2024-05-01', '2024-06-01')

        self.projet1.ajouter_membre_equipe(self.membre1)
        self.projet1.ajouter_membre_equipe(self.membre2)
        self.projet1.ajouter_tache(self.tache1)
        self.projet1.ajouter_tache(self.tache2)

        self.projet2.ajouter_membre_equipe(self.membre3)
        self.projet2.ajouter_membre_equipe(self.membre4)

    def test_ajouter_membre(self):
        nouveau_membre = Membre("Mami Awa Watt", "Developpeuse")
        self.equipe.ajouter_membre(nouveau_membre)
        self.assertIn(nouveau_membre, self.equipe.obtenir_membres())

    def test_ajouter_tache(self):
        tache3 = Tache("authentification", "Implémentation du module d'authentification", '2024-05-03', '2024-05-30', self.membre1, "Non commencé")
        self.projet1.ajouter_tache(tache3)
        self.assertIn(tache3, self.projet1.taches)

    def test_definir_budget(self):
        budget = 60000.0
        self.projet1.definir_budget(budget)
        self.assertEqual(self.projet1.budget, budget)

    def test_ajouter_risque(self):
        risque = Risque("Risque élevé", 0.8, "Critique")
        self.projet1.ajouter_risque(risque)
        self.assertIn(risque, self.projet1.risques)

    def test_ajouter_jalon(self):
        jalon = Jalon("phase 1 terminé", '2024-06-01')
        self.projet1.ajouter_jalon(jalon)
        self.assertIn(jalon, self.projet1.jalons)

    def test_enregistrer_changement(self):
        description = "Changement de la portée du projet"
        version_initiale = self.projet1.version
        self.projet1.enregistrer_changement(description)
        self.assertEqual(self.projet1.changements[-1].description, description)
        self.assertEqual(self.projet1.version, version_initiale + 1)

    def test_generer_rapport_performance(self):
        rapport = self.projet1.generer_rapport_performance()
        self.assertIn("Rapport de performance du projet Gestion des vacataires", rapport)
        self.assertIn("Version : 1", rapport)
        self.assertIn("Dates : 2024-05-01 à 2024-06-01", rapport)
        self.assertIn("Budget : 0.0 FCFA", rapport)
        self.assertIn("Équipe :", rapport)
        self.assertIn("Taches :", rapport)

    if __name__ == "__main__":
        unittest.main()