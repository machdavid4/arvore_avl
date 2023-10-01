class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def inserir(self, raiz, chave):
        if not raiz:
            return No(chave)
        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            raiz.direita = self.inserir(raiz.direita, chave)

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balanceamento = self.fator_balanceamento(raiz)

        if balanceamento > 1:
            if chave < raiz.esquerda.chave:
                return self.rotacao_direita(raiz)
            else:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
                return self.rotacao_direita(raiz)
        if balanceamento < -1:
            if chave > raiz.direita.chave:
                return self.rotacao_esquerda(raiz)
            else:
                raiz.direita = self.rotacao_direita(raiz.direita)
                return self.rotacao_esquerda(raiz)

        return raiz

    def remover(self, raiz, chave):
        if not raiz:
            return raiz

        if chave < raiz.chave:
            raiz.esquerda = self.remover(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.remover(raiz.direita, chave)
        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp

            temp = self.no_com_chave_minima(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = self.remover(raiz.direita, temp.chave)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balanceamento = self.fator_balanceamento(raiz)

        if balanceamento > 1:
            if self.fator_balanceamento(raiz.esquerda) >= 0:
                return self.rotacao_direita(raiz)
            else:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
                return self.rotacao_direita(raiz)
        if balanceamento < -1:
            if self.fator_balanceamento(raiz.direita) <= 0:
                return self.rotacao_esquerda(raiz)
            else:
                raiz.direita = self.rotacao_direita(raiz.direita)
                return self.rotacao_esquerda(raiz)

        return raiz

    def no_com_chave_minima(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def buscar(self, raiz, chave):
        if not raiz or raiz.chave == chave:
            return raiz
        if raiz.chave < chave:
            return self.buscar(raiz.direita, chave)
        return self.buscar(raiz.esquerda, chave)

    def inserir_chave(self, chave):
        self.raiz = self.inserir(self.raiz, chave)

    def remover_chave(self, chave):
        self.raiz = self.remover(self.raiz, chave)

    def buscar_chave(self, chave):
        return self.buscar(self.raiz, chave)

    def travessia_em_ordem(self, raiz):
        if raiz:
            self.travessia_em_ordem(raiz.esquerda)
            print(raiz.chave)
            self.travessia_em_ordem(raiz.direita)

    def imprimir_arvore(self):
        self.travessia_em_ordem(self.raiz)

arvore_avl = ArvoreAVL()
arvore_avl.inserir_chave(10)
arvore_avl.inserir_chave(20)
arvore_avl.inserir_chave(30)
arvore_avl.imprimir_arvore()
arvore_avl.remover_chave(20)
print()
arvore_avl.imprimir_arvore()