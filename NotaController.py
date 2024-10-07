from model.NotaMedia import NotaMedia

class NotaController:
    def __init__(self):
        self._nota_media = NotaMedia()

    def validar_notas(self):
        if self._nota_media.nota1 is None or self._nota_media.nota2 is None or self._nota_media.nota3 is None:
            raise ValueError("Todas as três notas devem ser fornecidas.")

    def calcular_media(self):
        self.validar_notas()
        return self._nota_media.calcular_media()

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"

    # Getters e Setters
    @property
    def nota_media(self):
        return self._nota_media

    @nota_media.setter
    def nota_media(self, valor):
        self._nota_media = valor
