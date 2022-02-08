class Ficha:
    def __init__(self,li,ld):
        self.__ld = ld
        self.__li = li

    #getter y setter ld .
    @property
    def ld(self):
        return self.__ld
    @ld.setter
    def ld(self,num):
        self.__ld = num
    #getter y setter li .
    @property
    def li(self):
        return self.__li
    @li.setter
    def li(self,num):
        self.__li = num

    #metodos
    def inventirFicha(self, ficha):
        return ficha[1],ficha[0]
    def mostrarFicha(self,):
        return self.li,self.ld

