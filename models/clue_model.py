from copy import deepcopy
from datetime import datetime


class Clue:
    def __init__(self, id, user_id, clue_text, key, date_created, is_solved=False):
        self.__id = id
        self.__user_id = user_id
        self.__clue_text = clue_text
        self.__key = key
        self.__date_created = date_created
        self.__is_solved = is_solved

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def clue_text(self):
        return self.__clue_text

    @property
    def key(self):
        return self.__key

    @property
    def date_created(self):
        return self.__date_created

    @property
    def is_solved(self):
        return self.__is_solved

    @is_solved.setter
    def is_solved(self, value):
        self.__is_solved = value


class ClueModel:
    def __init__(self):
        self.__clues = []
        self.__current_clue = None
        self.GenerateClues()

    @property
    def clues(self):
        return self.__clues

    @property
    def current_clue(self):
        return deepcopy(self.__current_clue)

    def GenerateClues(self):
        sample_clues = [
            (
                "I have keys but no locks. I have a space but no room. You can enter, but never leave.",
                "Keyboard",
            ),
            (
                "The more of me there is, the less you see.",
                "Darkness",
            ),
            (
                "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me.",
                "Fire",
            ),
            (
                "What has to be broken before you can use it?",
                "Egg",
            ),
            (
                "I'm tall when I'm young, and I'm short when I'm old. What am I?",
                "Candle",
            ),
            (
                "What is always in front of you but can't be seen?",
                "Future",
            ),
            (
                "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish.",
                "Map",
            ),
        ]

        self.__clues = [
            Clue(
                id=index + 1,
                user_id=0,
                clue_text=clue_text,
                key=key,
                date_created=datetime.now(),
            )
            for index, (clue_text, key) in enumerate(sample_clues)
        ]
        self.__current_clue = self.__clues[0] if self.__clues else None

    def GetCurrentClue(self):
        return deepcopy(self.__current_clue)

    def GetCurrentClueUsername(self):
        return "guest"

    def AddClue(self, clue_text: str, key: str, user_id: int):
        next_id = self.__clues[-1].id + 1 if self.__clues else 1
        clue = Clue(
            id=next_id,
            user_id=user_id,
            clue_text=clue_text,
            key=key,
            date_created=datetime.now(),
        )

        self.__clues.append(clue)

        if self.__current_clue is None:
            self.__current_clue = clue

        return True

    def AttemptCurrentClueSolve(self, key: str):
        if self.__current_clue is None:
            return False

        if key.strip().lower() == self.__current_clue.key.strip().lower():
            self.__current_clue.is_solved = True
            return True

        return False


if __name__ == "__main__":
    test_model = ClueModel()
    current_clue = test_model.GetCurrentClue()

    print(test_model.GetCurrentClueUsername())
    print(current_clue.clue_text if current_clue else None)
    print(test_model.AttemptCurrentClueSolve("Keyboard"))