from typing import List

def minHeightShelves(books: List[List[int]], shelfWidth: int) -> int:
    # 获取书籍的数量
    n = len(books)
    # 初始化动态规划数组，dp[i] 表示前 i 本书摆放的最小高度
    dp = [0] * (n + 1)

    # 遍历每一本书
    for i, (w, h) in enumerate(books, 1):
        # 初始假设当前这本书单独放在新的一层，高度为前 i-1 本书的最小高度加上当前书的高度
        dp[i] = dp[i - 1] + h

        # 尝试将当前书和前面的书放在同一层
        for j in range(i - 1, 0, -1):
            # 获取前一本书的宽度和高度
            prev_w, prev_h = books[j - 1]
            # 更新当前层的总宽度
            w += prev_w

            # 如果总宽度超过书架宽度，则停止尝试
            if w > shelfWidth:
                break

            # 更新当前层的最大高度
            h = max(h, prev_h)
            # 更新 dp[i] 为当前值和将前 j-1 本书放在前面层，当前层高度为 h 的较小值
            dp[i] = min(dp[i], dp[j - 1] + h)

    # 返回前 n 本书摆放的最小高度
    return dp[n]

if __name__ == '__main__':
    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth = 4
    print(minHeightShelves(books, shelfWidth))