def autocomplete_list(input, master_list):
    if not input:
        return []
    input = input.lower()
    return sorted([word for word in master_list if word.lower().startswith(input)])


def test_autocomplete_list():
    master_list = ["Maria", "Anna", "Anders", "Oskar"]
    input_value = "An"
    expected_output = ["Anders", "Anna"]

    result = autocomplete_list(input_value, master_list)

    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {result}")

    assert result == expected_output, f"Test failed: {result} != {expected_output}"


# Kör testet
test_autocomplete_list()








