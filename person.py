class Person:
    def __init__(self, name, age, job=None, pay=10):
        self.name = name
        self.age = age
        self.job = job
        self.pay = pay

    def get_subname(self):
        subname = self.name.split()[-1]
        return subname

    def rise_pay(self, persent):
        self.pay = float(self.pay + (self.pay * (persent / 100)))

    def __str__(self):
        s = "Person: {name}, {age} is now working as {job} with {pay:.2f} $/per hour".format(
            name=self.name, age=self.age, job=self.job, pay=self.pay
        )
        return s


class Manager(Person):
    def rise_pay(self, percent, bonus=10):
        Person.rise_pay(self, percent + bonus)


if __name__ == "__main__":
    bob = Person("Bob Ross", age=18, job="Freelancer", pay=17)
    # Overload of __str__ method

    pat = Manager(
        "Jeremi Rhiner", age=28, job="Hard Worker at Chemical Factory", pay=40
    )

    for person in (bob, pat):
        person.rise_pay(10)
        print(person)
