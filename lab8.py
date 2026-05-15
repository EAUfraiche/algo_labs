def solve():
    # Відкриваємо файл для читання
    try:
        with open('ijones.in', 'r') as f_in:
            # Зчитуємо всі слова з файлу в один список
            data = f_in.read().split()
    except FileNotFoundError:
        return

    if not data:
        return

    # Перші два значення — це W та H
    w = int(data[0])
    h = int(data[1])
    
    # Решта — це рядки коридору
    grid = data[2:]

    # dp[r] — кількість шляхів до плитки в рядку r поточного стовпця
    dp = [0] * h
    # char_sums — сумарна кількість шляхів до всіх попередніх плиток з літерами a-z
    char_sums = [0] * 26

    # Ініціалізація першого стовпця
    for r in range(h):
        dp[r] = 1
        # Якщо стовпців більше одного, готуємо суми для наступних кроків
        if w > 1:
            char_idx = ord(grid[r][0]) - ord('a')
            char_sums[char_idx] += 1

    # Основний цикл обробки стовпців (від 1 до W-1)
    for c in range(1, w):
        new_dp = [0] * h
        prev_col_total = sum(dp) # Сума всіх шляхів до попереднього стовпця
        
        # Тимчасовий масив для накопичення сум поточного стовпця
        current_col_char_sums = [0] * 26

        for r in range(h):
            current_char = grid[r][c]
            char_idx = ord(current_char) - ord('a')
            
            # 1. Шляхи кроком вправо + 2. Шляхи стрибком на таку ж літеру
            ways = prev_col_total + char_sums[char_idx]
            
            # Віднімаємо дублікат, якщо плитка зліва має таку ж літеру
            if grid[r][c-1] == current_char:
                ways -= dp[r]
            
            new_dp[r] = ways
            current_col_char_sums[char_idx] += ways

        # Додаємо результати поточного стовпця до загальної статистики літер
        for i in range(26):
            char_sums[i] += current_col_char_sums[i]
        
        dp = new_dp

    # Рахуємо фінальний результат
    if h == 1:
        result = dp[0]
    else:
        result = dp[0] + dp[h-1]

    # Записуємо результат у файл ijones.out
    with open('ijones.out', 'w') as f_out:
        f_out.write(str(result) + '\n')

if __name__ == "__main__":
    solve()