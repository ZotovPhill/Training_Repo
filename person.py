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
        uptime = float(self.pay + (self.pay * (persent / 100)))
        return uptime

    def __str__(self):
        s = "Person: {name}, {age} is now working as {job} with {pay} $/per hour".format(
            name=self.name, age=self.age, job=self.job, pay=self.pay
        )
        return s


if __name__ == "__main__":
    bob = Person("Bob Ross", age=18, job="Freelancer", pay=17)
    print(bob)  # Overload of __str__ method
    print("{0}, {1}".format(bob.name, bob.pay))
    print("{0}, {1:.2f}".format(bob.get_subname(), bob.rise_pay(10)))
