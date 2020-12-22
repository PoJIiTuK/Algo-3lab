def duplicate(male_in_tribe, female_in_tribe):
    return (male * female for male, female in zip(male_in_tribe, female_in_tribe))


def male_amount(tribe):
    return len({male_count for male_count in tribe if male_count % 2})


def female_amount(tribes):
    return len({female_count for female_count in tribes if not female_count % 2})
