class Student:
    # [assignment] Skeleton class. Add your code here
    #Constructor
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
        Print("my name is ", name, "and I'm ", age, "these are my track", track, "and scored", score,)

    # Method 
    def change_name(self, new_name):
        self.name = new_name
        return(self.name)

    def change_age(self, new_age):
        self.age = new_age
        return(self.age)

    def add_track(self, new_track):
        self.track = new_track
        return(self.track)

    def get_score(self, get_score):
        self.score = get_score
        return(self.score)

        

Bob = Student("Bob", 26, ["PY","CONDA"], 20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score(30.00))

