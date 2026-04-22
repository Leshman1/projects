class LZ77:

    def encode(self, data):
        i = 0
        res = []
        n = len(data)

        while i < n:
            # если последний символ
            if i == n - 1:
                res.append((0, 0, data[i]))
                break

            max_repeat = 0
            max_offset = 0

            # ищем лучшее совпадение
            for pos in range(i):
                repeat = 0
                while (i + repeat < n and
                       pos + repeat < i and
                       data[pos + repeat] == data[i + repeat]):
                    repeat += 1

                if repeat > max_repeat:
                    max_repeat = repeat
                    max_offset = i - pos

            if i + max_repeat >= n:
                max_repeat -= 1

            if max_repeat > 0:
                next_char = data[i + max_repeat]
                res.append((max_offset, max_repeat, next_char))
            else:
                res.append((0, 0, data[i]))

            i += max_repeat + 1

        return res

    def decode(self, data):
        res = []

        for offset, length, next_char in data:
            if length > 0:
                start = len(res) - offset
                for j in range(start, start + length):
                    res.append(res[j])               
            if next_char:
                res.append(next_char)
        return ''.join(res)


# тест
lz = LZ77()

print(lz.encode('abbabaabbaa'))
print(lz.decode([(0, 0, 'a'), (0, 0, 'b'), (1, 1, 'a'), (2, 2, 'a'), (6, 3, 'a')]))
print(lz.decode([(0,0,'a'),(0,0,'b'),(2,1,'a'),(3,2,'b'),(0,0,'a')]))