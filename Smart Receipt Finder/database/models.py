class Recipe:
    def __init__(self, recipe_id, name, ingredients, steps, image, category, favorite=0):
        self.id = recipe_id
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.image = image
        self.category = category
        self.favorite = favorite

    @classmethod
    def from_db_row(cls, row):
        return cls(
            recipe_id=row[0],
            name=row[1],
            ingredients=row[2],
            steps=row[3],
            image=row[4],
            category=row[5],
            favorite=row[6]
        )