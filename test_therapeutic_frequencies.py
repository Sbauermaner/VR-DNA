from therapeutic_frequencies import therapeutic_frequencies

def test_therapeutic_frequencies():
    try:
        therapeutic_frequencies()
        print("Тест успешно пройден!")
    except Exception as e:
        print(f"Ошибка теста: {e}")

test_therapeutic_frequencies()
