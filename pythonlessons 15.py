class Game:
    __true_answer = 0
    __false_answer = 0

    def test(self):
        question_list = ['15+24=?','5*6=?','100/10=?','132+18=?']
        for i in range(0, len(question_list)):
            print(question_list[i])
            answer = int(input('your answer is? -'))

            if answer == question_list[i]:
                pass
