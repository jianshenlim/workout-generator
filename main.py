import random
import os
import glob


class workoutApp:

    categories = []
    generatedworkout = []

    def addCategory(self):
        newCategory = input("Enter New Category Name: ")
        filecategory = str(newCategory) + ".txt"
        existingCat = self.getAllCategories()
        if filecategory in existingCat:
            print("Category already exists")
        else:
            f = open(filecategory, "x")
            print("New category: " + newCategory + " added")

    def addExercise(self,workout, category):
        with open(category) as file:
            contents = file.read()
            if workout in contents:
                print("Workout already exists")
            else:
                f = open(category, "a")
                f.write(workout + "\n")
                f.close()
                print("Exercise added")
        file.close()

    def deleteWorkout(self,workout, category):
        with open(category, "r") as file:
            exercises = file.readlines()
            file.close()
        with open(category, "w") as file:
            for exercise in exercises:
                if exercise.strip("\n") != workout:
                    file.write(exercise)
        print("Workout deleted")
        file.close()

    def getAllWorkOuts(self,category):
        workoutlist = []
        with open(category, "r") as file:
            exercises = file.readlines()
            for exercise in exercises:
                workoutlist.append(exercise.rstrip("\n"))
        file.close()

        return workoutlist

    def getRandomExercise(self,categoryName, number, mode):
        workoutlist = self.getAllWorkOuts(categoryName)
        if number > len(workoutlist):
            if mode == 0:
                print("Less than " + str(number) + " number of workout saved")
            else:
                print("Less than " + str(number) + " number of workout saved, all workouts added")
                return workoutlist
        else:
            exercises = random.sample(workoutlist, number)
            if mode == 0:
                print("")
                for exercise in exercises:
                    print(exercise)
                print("")
            else:
                return exercises

    def getAllCategories(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(dir_path)
        myCategories = glob.glob('*.txt')
        return myCategories

    def displayAllExercises(self,category):
        with open(category, "r") as file:
            exercises = file.readlines()
            print("Category: " + category[0:-4])
            for exercise in exercises:
                output = exercise.rstrip("\n")
                print(output)
        file.close()

    def displayAllExercisesInCat(self):
        self.generateDynamicList()
        category = int(input("Select Category to view: "))
        category -= 1
        if category >= 0 or category < len(self.categories):
            self.displayAllExercises(self.categories[category])
        else:
            print("Invalid category chosen")
            return

    def generateDynamicList(self):
        self.categories = self.getAllCategories()
        for x in range (len(self.categories)):
            print(str(x+1)+": " + self.categories[x][0:-4])

    def addExerciseToCategory(self):
        self.generateDynamicList()
        category = int(input("Select Category to add: "))
        category -= 1
        exercise = input("Enter exercise: ")
        if category >= 0 or category < len(self.categories):
            self.addExercise(exercise, self.categories[category])
        else:
            print("Invalid category chosen")
            return

    def deleteExerciseFromCategory(self):
        self.generateDynamicList()
        category = int(input("Select Category: "))
        category -= 1
        if category >= 0 or category < len(self.categories):
            self.displayAllExercisesInCat(self.categories[category])
            workout = input("Enter exercise to delete: ")
            self.deleteWorkout(workout, self.categories[category])
        else:
            print("Invalid category chosen")
            return


    def generateRandomExercises(self):
        self.generateDynamicList()
        category = int(input("Select Category: "))
        category -= 1
        number = int(input("Select number of exercises: "))
        if category >= 0 or category < len(self.categories):
            categoryFile = self.categories[category]
            self.getRandomExercise(categoryFile, number,0)
        else:
            print("Invalid category chosen")
            return

    def deleteCategory(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.generateDynamicList()
        category = int(input("Select Category: "))
        category -= 1
        if category >= 0 and (category < len(self.categories)):
            os.remove(dir_path + "\\" + self.categories[category])
            print("Category Deleted")
        else:
            print("Invalid category chosen")
            return

    def createWorkOut(self):
        print("List of Categories")
        self.generateDynamicList()
        workoutSelection = []
        for x in range (len(self.categories)):
            count = int(input("Enter number of workouts from category " + str(x+1) +": "))
            diff = int(input("Enter Difficulty Level (1-3): "))
            if diff < 1:
                diff = 1
            if diff > 3:
                diff = 3
            selection = (self.getRandomExercise(self.categories[x],count,1))
            for y in range (len(selection)):
                selection[y] = (selection[y],self.difficultyGenerator(diff))
            workoutSelection = workoutSelection + selection
        print("Workout Generated")
        self.generatedworkout = workoutSelection

    def saveWorkout(self):
        if len(self.generatedworkout) == 0:
            print("No workout to save")
        else:
            f = open("workout.txt","w")
            for exercise in self.generatedworkout:
                string = '{0:20} {1}'.format(exercise[0], exercise[1])
                f.write(string+"\n")
            print("Workout saved")
            f.close()

    def randomizeOrder(self):
        if len(self.generatedworkout) == 0:
            print("No workout to randomize")
        else:
            random.shuffle(self.generatedworkout)
            print("Workout randomized")

    def difficultyGenerator(self,type):
        if type == 1:
            repRange = [10,15,20]
            setMin = 8
            setMax = 10
            reps = random.choice(repRange)
            sets = random.randint(setMin,setMax)
        elif type == 2:
            repMin, repMax = 5,10
            setMin, setMax = 5,8
            reps = random.randint(repMin,repMax)
            sets = random.randint(setMin,setMax)
        else:
            repMin,setMin = 1,1
            repMax,setMax = 5,5
            reps = random.randint(repMin, repMax)
            sets = random.randint(setMin, setMax)

        diff = str(sets) + "x" + str(reps)
        return diff

    def displayWorkOut(self):
        if len(self.generatedworkout) == 0:
            print("No workout generated")
        else:
            for exercise in self.generatedworkout:
                print('{0:20} {1}'.format(exercise[0], exercise[1]))

    def mainMenu(self):
        print("\n----------------------------------")
        print("Workout Generator")
        print("----------------------------------")
        print("1: Get Random Exercise")
        print("2: Add Exercise")
        print("3: Category Options")
        print("4: Workout Options")
        print("0: Quit\n")

    def categoryMenu(self):
        print("\n1: Add Category")
        print("2: Delete Category")
        print("3: View Category Exercises")
        print("Any Other Button to Return\n")

    def workOutMenu(self):
        print("\n1: View Generated Workout")
        print("2: Randomize Current Workout")
        print("3: Generate Workout")
        print("4: Save Workout")
        print("Any Other Button to Return\n")

    def main(self):
        running = True
        while running:
            self.mainMenu()
            userChoice = int(input("Enter Selection Number: "))
            if userChoice == 1:
                self.generateRandomExercises()
            elif userChoice == 2:
                self.addExerciseToCategory()
            elif userChoice == 3:
                submenuRun = True
                while submenuRun:
                    self.categoryMenu()
                    subChoice = int(input("Enter Selection Number: "))
                    if subChoice == 1:
                        self.addCategory()
                    elif subChoice == 2:
                        self.deleteCategory()
                    elif subChoice == 3:
                        self.displayAllExercisesInCat()
                    else:
                        submenuRun = False

            elif userChoice == 4:
                submenuRun = True
                while submenuRun:
                    self.workOutMenu()
                    subChoice = int(input("Enter Selection Number: "))
                    if subChoice == 1:
                        self.displayWorkOut()
                    elif subChoice == 2:
                        self.randomizeOrder()
                    elif subChoice == 3:
                        self.createWorkOut()
                    elif subChoice == 4:
                        self.saveWorkout()
                    else:
                        submenuRun = False
            elif userChoice == 0:
                running = False
            else:
                continue

test = workoutApp()
test.main()
# test.generateRandomExercises()
# test.addExerciseToCategory()

# test.deleteExerciseFromCategory()

# test.createWorkOut()
# test.difficultyGenerator(3)

