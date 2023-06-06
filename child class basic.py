class clge:
    def psg(self):
        print("coimbatore")

class students(clge):
    def dep(self):
        print("robotics and automation")


class students1 (students):
    def mech(self):
        print("mechanical")


a=students1()
a.psg()
a.dep()
a.mech()
