from numpy import random


def monty_hall(attempts):
    no_change = []
    changed = []

    for i in range(0, attempts):
        car = random.choice(['Door 1', 'Door 2', 'Door 3'])  # car placed in a random door

        first_selection = random.choice(['Door 1', 'Door 2', 'Door 3'])  # contestant selects a random door

        # host opens a different door than contestant's choice and the one with the car
        host_opens = list({'Door 1', 'Door 2', 'Door 3'} - {first_selection, car})[0]

        # other door different from contestant's choice and not the opened door.
        other_door = list({'Door 1', 'Door 2', 'Door 3'} - {first_selection, host_opens})[0]

        # add true if contestant did not and won the prize
        no_change.append(first_selection == car)

        # add true if contestant changed the door and won the prize
        changed.append(other_door == car)

    print("ORIGINAL")
    print(attempts, "attempts were done")
    print("Chances of winning with first selection:" + str(sum(no_change) / attempts * 100))
    print("Chances of winning changing the selection:" + str(sum(changed) / attempts * 100))


def monty_hall_extra(attempts):
    no_change = []
    changed = []
    host_opened_car = []

    for i in range(0, attempts):
        car = random.choice(['Door 1', 'Door 2', 'Door 3', 'Door 4'])

        first_selection = random.choice(['Door 1', 'Door 2', 'Door 3', 'Door 4'])

        host_opens = random.choice(list({'Door 1', 'Door 2', 'Door 3', 'Door 4'} - {first_selection}))

        host_opened_car.append(host_opens == car)

        if host_opens != car:

            other_door1 = list({'Door 1', 'Door 2', 'Door 3', 'Door 4'} - {first_selection, host_opens})[0]
            other_door2 = list({'Door 1', 'Door 2', 'Door 3', 'Door 4'} - {first_selection, host_opens})[1]

            no_change.append(first_selection == car)

            changed.append(other_door1 == car)
            changed.append(other_door2 == car)

    print("EXTRA DOOR")
    print(attempts, "attempts were done")
    print("Host opened the prize:" + str(sum(host_opened_car) / attempts * 100))
    print("Chances of winning with first selection:" + str(sum(no_change) / attempts * 100))
    print("Chances of winning changing the selection:" + str(sum(changed) / attempts * 100))


if __name__ == '__main__':
    monty_hall(100000)
    monty_hall_extra(100000)
