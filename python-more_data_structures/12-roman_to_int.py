def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    deyerler = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    cem = 0
    uzunluq = len(roman_string)
    
    for i in range(uzunluq):
        cari_qiymet = deyerler.get(roman_string[i], 0)
        
        if i + 1 < uzunluq and cari_qiymet < deyerler.get(roman_string[i+1], 0):
            cem -= cari_qiymet
        else:
            cem += cari_qiymet
            
    return cem
