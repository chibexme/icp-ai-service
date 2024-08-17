from pydantic import BaseModel

from schema import MealPlanRequest


class MealPlan(BaseModel):
    day1: str
    day2: str
    day3: str
    day4: str
    day5: str
    day6: str
    day7: str


def meal_plan():
    return {
        "type": "function",
        "function": {
            "name": "provide_meal_plan",
            "description": "Curate a meal plan based on the information provided.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day1": {
                        "type": "string",
                        "description": "meals for day 1",
                    },
                    "day2": {
                        "type": "string",
                        "description": "meals for day 2",
                    },
                    "day3": {
                        "type": "string",
                        "description": "meals for day 3",
                    },
                    "day4": {
                        "type": "string",
                        "description": "meals for day 4",
                    },
                    "day5": {
                        "type": "string",
                        "description": "meals for day 5",
                    },
                    "day6": {
                        "type": "string",
                        "description": "meals for day 6",
                    },
                    "day7": {
                        "type": "string",
                        "description": "meals for day 7",
                    },
                },
                "required": ["day1", "day2", "day3", "day4", "day5", "day6", "day7"],
            },
        },
    }


def provide_meal_plan(data: MealPlan):
    return data


def meal_plan_cmd(req: MealPlanRequest):
    prompt = f"Provide a meal plan based on the following information: {req}"
    return prompt
