def brute_force(people_list, length):
    families = []

    for people in people_list:
        if length > 1000:
            print("To much families")
            break
        for family in families:

            if people[0] in family:
                family.add(people[1])

                break

            elif people[1] in family:
                family.add(people[0])

                break

        else:

            families.append(set((people[0], people[1])))

    return families
