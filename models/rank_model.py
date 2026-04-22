
class RankModel:
    def __init__(self, points):
        self.__current_points = points
        self.__ranks = {
            'Bystander': 0,
            'Inquisitor': 100,
            'Cryptic': 300,
            'Cipher-Smith': 500,
            'Oracle': 700
        }

    @property
    def curent_points(self):
        return self.__current_points

    @property
    def current_rank(self):
        prev_rank = list(self.__ranks.keys())[0]
        for rank, points_needed in self.__ranks.items():
            if self.__current_points < points_needed:
                return prev_rank
            else:
                prev_rank = rank

        return rank

if __name__ == "__main__":
    test_rank = RankModel(705)
    print(test_rank.current_rank)