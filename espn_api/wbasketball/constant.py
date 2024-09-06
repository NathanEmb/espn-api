POSITION_MAP = {
    0: "",
    1: "G",
    2: "F",
    3: "C",
    4: "F/C",
    5: "UTIL",
    6: "BE",
    7: "IR",
    8: "Unknown",
    9: "Unknown",
    # reverse
    "G": 1,
    "F": 2,
    "C": 3,
    "F/C": 4,
    "UTIL": 5,
    "BE": 6,
    "IR": 7,
}

PRO_TEAM_MAP = {
    0: "FA",
    3: "Dal",
    5: "Ind",
    6: "LA",
    8: "Min",
    9: "NY",
    11: "Phx",
    14: "Sea",
    16: "Wsh",
    17: "LV",
    18: "Conn",
    19: "Chi",
    20: "Atl",
}

STATS_MAP = {
    "0": "PTS",
    "1": "BLK",
    "2": "STL",
    "3": "AST",
    "4": "OREB",
    "5": "DREB",
    "6": "REB",
    "7": "EJ",
    "8": "FF",
    "9": "PF",
    "10": "TF",
    "11": "TO",
    "12": "DQ",
    "13": "FGM",
    "14": "FGA",
    "15": "FTM",
    "16": "FTA",
    "17": "3PM",
    "18": "3PA",
    "19": "FG%",
    "20": "FT%",
    "21": "3PT%",
    "22": "AFG%",
    "23": "FGMI",
    "24": "FTMI",
    "25": "3PMI",
    "26": "APG",
    "27": "BPG",
    "28": "MPG",
    "29": "PPG",
    "30": "RPG",
    "31": "SPG",
    "32": "TOPG",
    "33": "3PG",
    "34": "PPM",
    "35": "A/TO",
    "36": "STR",
    "37": "DD",
    "38": "TD",
    "39": "QD",
    "40": "MIN",
    "41": "GS",
    "42": "GP",
    "43": "TW",
    "44": "FTR",
    "45": "45",
}

STAT_ID_MAP = {"10": "projected", "01": "last_7", "02": "last_15", "03": "last_30"}

ACTIVITY_MAP = {
    178: "FA ADDED",
    180: "WAIVER ADDED",
    179: "DROPPED",
    181: "DROPPED",
    239: "DROPPED",
    244: "TRADED",
    "FA": 178,
    "WAIVER": 180,
    "TRADED": 244,
}
