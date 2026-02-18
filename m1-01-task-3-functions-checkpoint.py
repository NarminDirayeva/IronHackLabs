def str_to_float(value):
    try :
        return float(value)

    except (ValueError, TypeError):
        return None

def cleaned_str(s):
    if not isinstance(s, str):
        return None
    return s.strip().lower()

tests=["  HelLo",1,-23,"",None,[3,4,5],True,0,2.43]
for i in tests:
    print(str_to_float(i))
    print(cleaned_str(i))