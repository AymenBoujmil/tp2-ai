import random
import Utils

class Game:
    def minValue(self, state,a,b,noeud_visite):
        if Utils.terminal(state):
            return 1
        v = 1
        for action in Utils.successors(state):
            v = min(v, self.maxValue(action,a,b,noeud_visite))
            noeud_visite[0] = noeud_visite[0] + 1
            if v <= a:
                return v
            b = min(b,v)
        return v

    def maxValue(self, state,a,b,noeud_visite):
        if Utils.terminal(state):
            return -1
        v = -1
        for action in Utils.successors(state):
            v = max(v, self.minValue(action,a,b,noeud_visite))
            noeud_visite[0] = noeud_visite[0] + 1
            if v >= b:
                return v
            a = max(a,v)
        return v

    def alpha_beta(self, state):
        noeud_visite = [0]
        v = -1
        for action in Utils.successors(state):
            if self.minValue(action, -1, 1, noeud_visite) > v:
                print('The AI has visited ',noeud_visite,' nodes!')
                return action
        choice = random.randint(0, len(Utils.successors(state))-1)
        print('The AI has visited ', noeud_visite, ' nodes!')
        return Utils.successors(state)[choice]

    def play(self, liste):
        start= input('do you want to play : 1- First 2- Second ')
        turn = True if int(start) == 1 else False
        current = liste
        print('the current list is : ', liste)
        choice =liste
        while not Utils.gameOver(current):

            if(turn):
                current = Utils.successors(choice)
                print("Your turn! choose an action:")
                i = 0
                for state in current:
                    i = i + 1
                    print(i, ") ", state)
                choice = int(input())
                current = current[choice-1]
                turn = False
            else:
                choice = self.alpha_beta(current)
                print("AI turn!", choice)
                current = choice
                turn = True
        result = "you lost!" if turn else "You won!"
        print(result)

def main():

    game = Game()
    game.play([15])


if __name__ == '__main__':
    main()