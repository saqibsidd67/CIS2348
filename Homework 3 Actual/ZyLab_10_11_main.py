# Saqib Siddiqui
# PSID: 1495537


class FoodItem:

    def __init__(self,name = 'None' , fat = 0.00 , carbs = 0.00 , protein = 0.00 ):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories


    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':

    food = FoodItem()
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    calories = float(input())


    food2 = FoodItem(name,fat,carbs,protein)
    servings = food.get_calories(calories)
    servings2 = food2.get_calories(calories)


    food.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(calories,servings))
    print()
    food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(calories, servings2))









