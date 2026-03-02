def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def has_three_sum(arr, P):
    """
    Перевіряє, чи існують у масиві три різні елементи,
    сума яких дорівнює числу P.
    """

    n = len(arr)

    if n < 3:
        return False

    bubble_sort(arr)

    for i in range(n - 2):

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == P:
                return True
            elif current_sum < P:
                left += 1
            else:
                right -= 1

    return False


if __name__ == "__main__":

    print("Введіть числа через пробіл.")
    print("Останнє число — це P (шукане значення).")
    print("Приклад: 1 2 3 6")

    data = list(map(int, input("Введіть числа: ").split()))

    if len(data) < 4:
        print("Потрібно мінімум 3 числа + P")
    else:
        *array, P = data

        if has_three_sum(array, P):
            print("Такі числа є")
        else:
            print("Таких чисел немає")