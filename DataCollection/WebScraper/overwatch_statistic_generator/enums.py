import enum

class GameModes(enum.Enum):
    QP = 0
    COMP = 1

class DataTables(enum.Enum):
    Combat = 0
    Game = 1
    HeroSpecific = 2
    Assists = 3

class Heroes(enum.Enum):
    All = 0
    Reaper = 1
    Tracer = 2
    Mercy = 3
    Hanzo = 4
    Torbjorn = 5
    Reinhardt = 6,
    Pharah = 7
    Winston = 8
    Widowmaker = 9
    Bastion = 10
    Symmetra = 11
    Zenyatta = 12
    Genji = 13
    Roadhog = 14
    McCree = 15
    Junkrat = 16
    Zarya = 17
    Soldier76 = 18
    Lucio = 19
    Dva = 20
    Mei = 21
    Sombra = 22
    Doomfist = 23
    Ana = 24
    Orisa = 25
    Moira = 26
    Brigitte = 27
    Ashe = 28
