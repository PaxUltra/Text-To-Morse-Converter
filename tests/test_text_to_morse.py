import text_to_morse

def test_encode_alphabet():
    text1 = "The quick brown fox jumps over a lazy dog"
    text2 = "Sphinx of black quartz, judge my vow"
    text3 = "How vexingly quick daft zebras jump"

    assert text_to_morse.encode(text1) == "- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / .- / .-.. .- --.. -.-- / -.. --- --."
    assert text_to_morse.encode(text2) == "... .--. .... .. -. -..- / --- ..-. / -... .-.. .- -.-. -.- / --.- ..- .- .-. - --.. --..-- / .--- ..- -.. --. . / -- -.-- / ...- --- .--"
    assert text_to_morse.encode(text3) == ".... --- .-- / ...- . -..- .. -. --. .-.. -.-- / --.- ..- .. -.-. -.- / -.. .- ..-. - / --.. . -... .-. .- ... / .--- ..- -- .--."

def test_encode_numbers():
    test_string = "1234567890"
    assert text_to_morse.encode(test_string) == ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"

def test_encode_punctuation():
    test_string = "&\'@)(:,=!.-*%+\"?/"
    assert text_to_morse.encode(test_string) == ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- -..- ----- -..-. ----- .-.-. .-..-. ..--.. -..-."

def test_decode_alphabet():
    test_code1 = "- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / .- / .-.. .- --.. -.-- / -.. --- --."
    test_code2 = "... .--. .... .. -. -..- / --- ..-. / -... .-.. .- -.-. -.- / --.- ..- .- .-. - --.. --..-- / .--- ..- -.. --. . / -- -.-- / ...- --- .--"
    test_code3 = ".... --- .-- / ...- . -..- .. -. --. .-.. -.-- / --.- ..- .. -.-. -.- / -.. .- ..-. - / --.. . -... .-. .- ... / .--- ..- -- .--."

    assert text_to_morse.decode(test_code1) == "THE QUICK BROWN FOX JUMPS OVER A LAZY DOG"
    assert text_to_morse.decode(test_code2) == "SPHINX OF BLACK QUARTZ, JUDGE MY VOW"
    assert text_to_morse.decode(test_code3) == "HOW VEXINGLY QUICK DAFT ZEBRAS JUMP"

def test_decode_numbers():
    test_code = "----- ----. ---.. --... -.... ..... ....- ...-- ..--- .----"
    assert text_to_morse.decode(test_code) == "0987654321"

def test_decode_punctuation():
    test_code = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- -..- ----- -..-. ----- .-.-. .-..-. ..--.. -..-."
    assert text_to_morse.decode(test_code) == "&\'@)(:,=!.-*%+\"?/"