# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not ((not(x <= z)) or (y == w) or (not y)):
#                     print(x, y, z, w)

# for i in range(100000):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n += '10'
#     else:
#         n = '1' + n + '01'
#     if int(n, 2) > 516:
#         print(i)
#         break


# for i in range(10000000):
#     s = i
#     s = (s - 10) // 7
#     n = 1
#     while s > 0:
#         n *= 2
#         s -= n
#     if n == 8:
#         print(i)
#         break


# s = '8' * 86
#
# while '1111' in s or '8888' in s:
#     if '1111' in s:
#         s = s.replace('1111', '8', 1)
#     else:
#         s = s.replace('8888', '11', 1)
#
# print(s)


# num = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 2 ** 1050 - 2022
# s = []
#
# while num > 0:
#     s.append(num % 4)
#     num //= 4
#
# print(s.count(3))


# def f(n):
#     if n < 3:
#         return 2
#     elif n > 2 and n % 2 == 0:
#         return f(n - 1) + f(n - 2) - n
#     elif n > 2 and n % 2 != 0:
#         return f(n - 2) - f(n - 1) - 2 * n
#
# print(f(30))


# s = list(map(int, open('17(8).txt').readlines()))
#
# mn17 = 99999999
# for i in s:
#     if i % 17 == 0:
#         mn17 = min(mn17, i)
#
# count = 0
# mx = 0
#
# for i in range(len(s) - 1):
#     if s[i] % mn17 == 0 or s[i + 1] % mn17 == 0:
#         count += 1
#         mx = max(mx, s[i] + s[i + 1])
#
# print(count, mx)


# for i in range(100000):
#     s = i
#     p = 10
#     q = 8
#     k1 = 0
#     k2 = 0
#     while s <= 100:
#         s += p
#         k1 += 1
#
#     while s >= q:
#         s -= q
#         k2 += 1
#     k1 += s
#     k2 += s
#
#     if k1 == 10 and k2 == 19:
#         print(i)
#         break


# s = open('24(2).txt').readline()
# for x in range(2):
#     count = 0
#     mx = 0
#     for i in range(x, len(s) - 1, 2):
#         if s[i] == 'A' and (s[i + 1] == 'B' or s[i + 1] == 'C'):
#             count += 1
#         else:
#             mx = max(mx, count)
#             count = 0
#     mx = max(mx, count)
#     print(mx)

# for x in range(10):
#     for y in range(10):
#         num = int(f'12345{x}6{y}8')
#         if num % 17 == 0:
#             print(num, num // 17)
