import easygui, random

people_killed = 0
health = 100

easygui.msgbox('''Ты хочешь получить меч Эскалибрус. Вы пошли к Священному камню.
Твоя попытка достать меч из камня не удалась. На нём было написано: 
\"Вы должны быть сильным если хотите получить его.\" Посовещавшись с жителями вы узнали, что Эскалибрусом 
владел Сильный волшебник. Именно он создал достопримечательность. 
Ещё вы узнали, что чтобы получить меч нужно выиграть в
нескольких дуэлях. Во скольких именно никто не знал. 
Поговорив ещё вы узнали, что кол-во дуэлей варьируется от 2 до 7.
Вы решили участвовать в дуэлях.
У вас есть шанс выиграть и есть шанс проиграть. 
При выборе лёгкой сложности вы уменьшете шанс проигрыша. При выборе сложной 
наоборот увеличите.
                                ЖЕЛАЕМ УДАЧИ''')

difficulty = easygui.choicebox(msg = "                       ВЫБЕРИТЕ СЛОЖНОСТЬ", choices = ("Легко", "Сложно"))
wins_need = random.randint(2, 7)

while True:
    if difficulty == "Легко":
        while True:
            if health != 0:
                action = easygui.buttonbox(msg = f'Ваше здоровье: {health} Кол-во выигранных дуэлей {people_killed}', choices = ("Дуэль", "Пойти к камню"))

                if action == "Дуэль" and health != 0:
                    luck = random.randint(1, 3)
                    if luck == 1:
                        health -= 50
                        easygui.msgbox("Дуэль проиграна!")
                    else:
                        people_killed += 1
                        easygui.msgbox("Вы выиграли дуэль!")
                else:
                    break
            else:
                break

    elif difficulty == "Сложно":
        while True:
            if health != 0:
                action = easygui.buttonbox(msg = f'Ваше здоровье: {health} Кол-во выигранных дуэлей {people_killed}', choices = ("Дуэль", "Пойти к камню"))

                if action == "Дуэль" and health != 0:
                    luck = random.randint(1, 2)
                    if luck == 1:
                        health -= 50
                        easygui.msgbox("Дуэль проиграна!")
                    else:
                        people_killed += 1
                        easygui.msgbox("Вы выиграли дуэль!")
                else:
                    break
            else:
                break

    if health == 0:
        easygui.msgbox("Вы умерли... Спасибо за игру...")
        health = 100
        people_killed = 0
        wins_need = random.randint(2, 7)
        

    elif action =="Пойти к камню":
        if wins_need <= people_killed:
            easygui.msgbox('''Вы подошли к камню. Вы смогли достать меч!
                ПОЗДРАВЛЯЕМ ВЫ ПОБЕДИЛИ!
    
            создатель terillic''')

            people_killed = 0
            health = 100
            wins_need = random.randint(2, 7)


        elif wins_need > people_killed:
            easygui.msgbox('''Вы подошли к камню. Вы не смогли достать меч!
                На этом и закончилась сказка...
                       
                       
        создатель terillic''')
            
        people_killed = 0
        health = 100
        wins_need = random.randint(2, 7)