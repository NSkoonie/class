#hw8p9
#Noah Schoonover

import random

#-------------------------------------------- Class Question

class Question():

    def __init__(self, question, correctAns, ans2, ans3, ans4):
        self.question = question
        self.answers = [correctAns, ans2, ans3, ans4]
        # randomize answers
        self.randomList = list(self.answers)    # you have to do this. setting var to list only creates reference
                                                # and changes made to either var affect the same list.
        random.shuffle(self.randomList)
        self.randomDic = {1 : self.randomList[0],
                          2 : self.randomList[1],
                          3 : self.randomList[2],
                          4 : self.randomList[3]}

    def __str__(self):
        return ('{}\n\n'
                '1) {}\n'
                '2) {}\n'
                '3) {}\n'
                '4) {}\n'.format(self.question,
                                 self.randomDic[1],
                                 self.randomDic[2],
                                 self.randomDic[3],
                                 self.randomDic[4]))
        
    def checkAnswer(self, a):
        if self.randomDic[a] == self.answers[0]:
            return True
        else:
            return False

#-------------------------------------------- Question Objects

questions = [] #questions are appended to list to eliminate variable names

questions.append(Question('Mark Zuckerberg was one of the founders of which social networking site?',
                          'Facebook',
                          'Snapchat',
                          'Instagram',
                          'Tumblr'))
questions.append(Question('What was the first console video game that allowed the game to be saved?',
                          'The Legend of Zelda',
                          'Mario',
                          'Donkey Kong',
                          'Oregon Trail'))
questions.append(Question('Regarding data storage, what does the acronym SSD stand for?',
                          'Solid State Drive',
                          'Secondary Stage Drive',
                          'Static Storage Device',
                          'SATA Storage Disk'))
questions.append(Question('Created in 2009, what was the first decentralized cryptocurrency?',
                          'Bitcoin',
                          'Webcoin',
                          'Etherbucks',
                          'DataDollars'))
questions.append(Question('What does the acronym USB stand for when referring to a computer port?',
                          'Universal Serial Bus',
                          'Uninterruptable Storage Base',
                          'Universal Storage Bank',
                          'Uvekurk Status Bank'))
questions.append(Question('What do you call the small image icons used to express emotions or ideas in digital communication?',
                          'Emoji',
                          'Smiley',
                          'Face',
                          'Icon'))
questions.append(Question('When referring to a computer monitor, what does the acronym LCD stand for?',
                          'Liquid Crystal Display',
                          'Limited Capacity Drive',
                          'Liquid Capsule Detector',
                          'Large Crown Display'))
questions.append(Question('When talking about computer memory, what does the acronym ROM stand for?',
                          'Read-Only Memory',
                          'Random Overclock Memory',
                          'Reference Only Memory',
                          'Rescue Octabyte Memory'))
questions.append(Question('In computer science, what does “GUI” stand for?',
                          'Graphical User Interface',
                          'Gigabyte Uval Instance',
                          'Gigantic User Inkspace',
                          'Generated User Instance'))
questions.append(Question('Small decorative lines on letters in some fonts are known as what?',
                          'Serifs',
                          'Sans',
                          'Tildes',
                          'Frills'))
                          
random.shuffle(questions)

#-------------------------------------------- getValidAnswer function

def getValidAnswer():
    
    gotValidAnswer = False
    while not gotValidAnswer:
        a = input(': ')
        try:
            a = int(a)
        except ValueError:
            print('Invalid Answer.')
        else:
            if a in [1, 2, 3, 4]:
                gotValidAnswer = True
                return a
            else:
                print('Invalid Answer.')


#-------------------------------------------- main function

def main():

    player1Points = 0
    player2Points = 0
    
    for q in range(len(questions)):
        if q < 5:
            player = 'Player 1'
        else:
            player = 'Player 2'
        print(player)
        print(questions[q])

        ans = getValidAnswer()
        
        if questions[q].checkAnswer(ans):
            print('Correct.\n')
            if player == 'Player 1':
                player1Points += 1
            else:
                player2Points += 1
        else:
            print('Incorrect.\n')

    print('\nPlayer 1: {} points\n'
          'Player 2: {} points\n'.format(player1Points, player2Points))

#-------------------------------------------- Run

main()

