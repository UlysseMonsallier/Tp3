class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None


class ListeChainee:
    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0

    def prepend(self, element):
        nouveau = Noeud(element)
        nouveau.suivant = self.tete
        self.tete = nouveau
        if self.queue is None:
            self.queue = nouveau
        self.taille += 1

    def append(self, element):
        nouveau = Noeud(element)
        if self.queue is None:
            self.tete = nouveau
            self.queue = nouveau
        else:
            self.queue.suivant = nouveau
            self.queue = nouveau
        self.taille += 1

    def pop_front(self):
        if self.tete is None:
            raise IndexError("pop_front sur une liste vide")
        valeur = self.tete.valeur
        self.tete = self.tete.suivant
        if self.tete is None:
            self.queue = None
        self.taille -= 1
        return valeur

    def peek(self):
        if self.tete is None:
            raise IndexError("peek sur une liste vide")
        return self.tete.valeur

    def est_vide(self):
        return self.tete is None

    def __len__(self):
        return self.taille

    def __repr__(self):
        elements = []
        courant = self.tete
        while courant is not None:
            elements.append(str(courant.valeur))
            courant = courant.suivant
        return " --> ".join(elements) + " --> None"