class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40
    def salad_info(self):
      print("{} potatoes,  {} celery, {}onions, {} special".format(self.potatoes, self.celery, self.onions, self.raisins))


x = SpecialPotatoSalad("2","3",4)
x.salad_info()
elattr(x,'raisins')
#x.salad_info(,0)





