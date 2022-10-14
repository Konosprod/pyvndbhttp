from pyvndbhttp import DbQuery, And, Or, Filter, QType
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
    print(api.Filters(filters).Results(5).Type(QType.VN).Request())
    

if __name__ == "__main__":
    main()