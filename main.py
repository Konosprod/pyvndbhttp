from pyvndbhttp import DbQuery, And, Or, Filter
import json

def main():
    api = DbQuery()
    filters = And(
                Or(
                    Filter("lang", "=", "en"), 
                    Filter("lang", "=", "de"), 
                    Filter("lang", "=", "fr")
                ), 
                Filter("olang", "!=", "ja"), 
                Filter("release", "=", 
                    And(
                        Filter("release", ">=", "2020-01-01"), 
                        Filter("producer", "=", 
                            Filter("id", "=", "p30")
                        )
                    )
                )
            )
    print(json.dumps(filters.tolist()))
    print(api.Sort(True).Results(15))
    

if __name__ == "__main__":
    main()