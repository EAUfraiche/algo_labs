def merge_sort(arr):
    """
    Сортує список методом злиття (Merge Sort).
    Повертає відсортований список.
    
    Складність:
    O(N log N)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Зливає два відсортовані списки у один відсортований.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def has_three_sum(arr, P):
    """
    Перевіряє, чи існують у масиві три різні елементи,
    сума яких дорівнює числу P.
    """
    n = len(arr)
    if n < 3:
        return False

    arr = merge_sort(arr)  

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