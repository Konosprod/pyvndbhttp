import requests
import json
       
class DbQuery():

    def __init__(self, type= "vn", filters = [], fields = "", sort = "",
    reverse = False, results = 10, page = 1, count = False, 
    compact_filters = False, normalized_filters = False):

        self._api_url = "https://beta.vndb.org/api/kana/"

        self._filters = filters
        self._fields = fields
        self._sort = sort
        self._reverse = reverse
        self._results = results
        self._page = page
        self._count = count
        self._compact_filters = compact_filters
        self._normalized_filters = normalized_filters
        self._type = "vn"

    def Get(self):
        r = requests.post(self._api_url + self._type)


    def Fields(self, fields):
        self._add_fields = True
        self._fields = fields
        return self

    def Sort(self, sort: str):
        """
        Field to sort on. Supported values depend on the type of data being queried
        """
        self._add_sort = True
        self._sort = sort
        return self

    def Reverse(self, reverse: bool):
        """
        Set to true to sort in descending order
        """
        self._add_reverse = True

        if type(reverse) is bool:
            self._reverse = reverse
        else:
            raise TypeError("Reverse must be boolean type")

        return self

    def Results(self, results: int):
        """
        Number of results per page, max 100
        """
        self._add_results = True

        if type(results) is int:
            if results <= 100 and results > 0:
                self._results = results
            else:
                raise ValueError("Results must be between 1 and 100")
        else:
            raise TypeError("Results must be int type")

        return self

    def Stats(self):
        r = requests.get(self._api_url + "stats")
        return r.json()

    def And(self, value):
        self._filters.append("and")
        self._filters.append(value)
        return self

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class And():
    def __init__(self, *args):
        self._list = []
        self._list.append("and")

        for arg in args:
            if isinstance(arg, Filter) or isinstance(arg, Or) or isinstance(arg, And):
                self._list.append(arg.tolist())
            else:
                self._list.append(arg)

    def __str__(self):
        r = "["

        for item in self._list:
            r += str(item)+","

        r = r[:-1]+"]"
        return r
    
    def tolist(self):
        return self._list

class Or():
    def __init__(self, *args):
        self._list = []
        self._list.append("or")

        for arg in args:
            if isinstance(arg, Filter) or isinstance(arg, Or) or isinstance(arg, And):
                self._list.append(arg.tolist())
            else:
                self._list.append(arg)

    def __str__(self):
        r = "["

        for item in self._list:
            r += str(item)+","

        r = r[:-1]+"]"
        return r

    def tolist(self):
        return self._list

                

class Filter():
    def __init__(self, name="", operator="", value=""):
        self._name = name
        self._operator = operator
        self._value = value

    def __str__(self):
        return str()
    
    def tolist(self):
        r = []
        r.append(self._name)
        r.append(self._operator)

        if isinstance(self._value, Filter) or isinstance(self._value, Or) or isinstance(self._value, And):
            r.append(self._value.tolist())
        else:
            r.append(self._value)

        return r

