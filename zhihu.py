import ctypes


class Func_s:
    def __init__(self, data):
        data.o = False


class Func_i:
    def __init__(self, data):
        self.t = (2048 & data) >> 11
        self.s = (1536 & data) >> 9
        self.i = 511 & data
        self.h = 511 & data

    def e(self, data):
        if 0 == self.t:
            data.r[self.s] = self.i
        elif 1 == self.t:
            data.r[self.s] = data.k[self.h]


class Func_h:
    def __init__(self, data):
        self.s = (3072 & data) >> 10
        self.h = 1023 & data

    def e(self, data):
        data.k[self.h] = data.r[self.s]


class Func_a:
    def __init__(self, data):
        self.a = (3072 & data) >> 10
        self.c = (768 & data) >> 8
        self.n = (192 & data) >> 6
        self.t = 63 & data

    def e(self, data):
        if 0 == self.t:
            data.r[self.a] = data.r[self.c] + data.r[self.n]
        elif 1 == self.t:
            data.r[self.a] = data.r[self.c] - data.r[self.n]
        elif 2 == self.t:
            data.r[self.a] = data.r[self.c] * data.r[self.n]
        elif 3 == self.t:
            data.r[self.a] = data.r[self.c] / data.r[self.n]
        elif 4 == self.t:
            data.r[self.a] = data.r[self.c] % data.r[self.n]
        elif 5 == self.t:
            data.r[self.a] = data.r[self.c] == data.r[self.n]
        elif 6 == self.t:
            data.r[self.a] = data.r[self.c] >= data.r[self.n]
        elif 7 == self.t:
            data.r[self.a] = data.r[self.c] or data.r[self.n]
        elif 8 == self.t:
            data.r[self.a] = data.r[self.c] and data.r[self.n]
        elif 9 == self.t:
            data.r[self.a] = data.r[self.c] != data.r[self.n]
        elif 10 == self.t:
            data.r[self.a] = False
        elif 11 == self.t:
            data.r[self.a] = data.r[self.c] in data.r[self.n]
        elif 12 == self.t:
            data.r[self.a] = data.r[self.c] > data.r[self.n]
        elif 13 == self.t:
            data.r[self.a] = - data.r[self.c]
        elif 14 == self.t:
            data.r[self.a] = data.r[self.c] < data.r[self.n]
        elif 15 == self.t:
            data.r[self.a] = data.r[self.c] & data.r[self.n]
        elif 16 == self.t:
            data.r[self.a] = data.r[self.c] ^ data.r[self.n]
        elif 17 == self.t:
            data.r[self.a] = int_overflow(data.r[self.c] << data.r[self.n])
        elif 18 == self.t:
            data.r[self.a] = unsigned_right_shift(data.r[self.c], data.r[self.n])
        elif 19 == self.t:
            data.r[self.a] = data.r[self.c] | data.r[self.n]
        elif 20 == self.t:
            data.r[self.a] = not data.r[self.c]


class Func_c:
    def __init__(self, data):
        self.s = data >> 10 & 3
        self.i = 1023 & data

    def e(self, data):
        data.Q.append(data.C)
        data.B.extend(data.k)
        data.C = data.r[self.s]
        data.k = []
        for t in range(self.i):
            data.k.insert(0, data.f.pop() if data.f else None)
        data.g.extend(data.f)
        data.f = []


class Func_n:
    def __init__(self):
        pass

    def e(self, data):
        data.C = data.Q.pop() if data.Q else None
        data.k = data.B.pop() if data.B else None
        data.f = data.g.pop() if data.g else None


class Func_e:
    def __init__(self, data):
        self.a = (3072 & data) >> 10
        self.c = (768 & data) >> 8
        self.t = 63 & data

    def e(self, data):
        if 0 == self.t:
            data.u = data.r[self.a] >= data.r[self.c]
        elif 1 == self.t:
            data.u = data.r[self.a] <= data.r[self.c]
        elif 2 == self.t:
            data.u = data.r[self.a] > data.r[self.c]
        elif 3 == self.t:
            data.u = data.r[self.a] < data.r[self.c]
        elif 4 == self.t:
            data.u = data.r[self.a] == data.r[self.c]
        elif 5 == self.t:
            data.u = data.r[self.a] != data.r[self.c]
        elif 6 == self.t:
            data.u = data.r[self.a]
        elif 7 == self.t:
            data.u = not data.r[self.a]


class Func_o:
    def __init__(self, data):
        self.h = (4095 & data) >> 2
        self.t = 3 & data

    def e(self, data):
        if 0 == self.t:
            data.C = self.h
        elif 1 == self.t:
            if data.u:
                data.C = self.h
        elif 2 == self.t:
            if not data.u:
                data.C = self.h
        elif 3 == self.t:
            data.C = self.h
            data.w = None

        data.u = False


class Func_r:
    def __init__(self, data):
        self.s = data >> 10 & 3
        self.i = data >> 2 & 255
        self.t = 3 & data

    def e(self, data):
        t = []
        if 0 == self.t:
            for n in range(self.i):
                t.insert(0, data.f.pop() if data.f else None)
            data.r[3] = data.r[self.s](t[0], t[1])
        elif 1 == self.t:
            r = data.f.pop() if data.f else None
            for n in range(self.i):
                t.insert(0, data.f.pop() if data.f else None)
            data.r[3] = data.r[self.s][r](t[0], t[1])
        elif 2 == self.t:
            for n in range(self.i):
                t.insert(0, data.f.pop() if data.f else None)
            data.r[3] = data.r[self.s](t[0], t[1])


class Func_Q:
    def __init__(self, data):
        self.t = (4095 & data) >> 10
        self.s = (1023 & data) >> 8
        self.i = 1023 & data
        self.h = 63 & data

    def e(self, data):
        if 0 == self.t:
            data.f.append(data.r[self.s])
        elif 1 == self.t:
            data.f.append(self.i)
        elif 2 == self.t:
            data.f.append(data.k[self.h])
        elif 3 == self.t:
            data.f.append(Func_k(data.b[self.h]))


class Func_C:
    def __init__(self, data):
        self.t = (4095 & data) >> 10
        self.a = (1023 & data) >> 8
        self.c = (255 & data) >> 6

    def e(self, data):
        t = data.f.pop() if data.f else None
        if 0 == self.t:
            data.r[self.a] = data.r[self.c][t]
        elif 1 == self.t:
            data.r[self.c][t] = data.f.pop() if data.f else None
        elif 2 == self.t:
            data.r[self.a] = eval(t)


class Func_B:
    def __init__(self, data):
        self.s = (3072 & data) >> 10
        self.h = (1023 & data)

    def e(self, data):
        data.r[self.s] = Func_k(data.b[self.h])


class Func_f:
    def __init__(self, data):
        self.h = 4095 & data

    def e(self, data):
        data.w = self.h


class Func_g:
    def __init__(self, data):
        self.s = (3072 & data) >> 10

    def e(self, data):
        pass


class Func_u:
    def __init__(self, data):
        self.h = 4095 & data

    def e(self, data, val):
        o = Func_G()
        o.k = [val]
        o.v(data.G, self.h, data.b)
        return o.r[3]

        # def r(r)


class Func_w:
    def __init__(self, data):
        self.t = (3840 & data) >> 8
        self.s = (192 & data) >> 6
        self.i = 63 & data

    def e(self, data):
        t = {}
        o = []
        if 0 == self.t:
            for n in range(self.i):
                t[data.f.pop()] = data.f.pop()
            data.r[self.s] = t
        elif 1 == self.t:
            for n in range(self.i):
                o.insert(0, data.f.pop())
            data.r[self.s] = o


def Func_k(data):
    n = []
    t = 66
    for r in range(len(data)):
        o = 24 ^ data[r] ^ t
        n.append(chr(o))
        t = o
    return "".join(n)


class Func_G:
    def __init__(self):
        self.r = [0, 0, 0, 0]
        self.C = 0
        self.Q = []
        self.k = []
        self.B = []
        self.f = []
        self.g = []
        self.G = [
            57351, 37632, 39936, 43008, 39937, 41984, 0, 4096, 8194, 39938, 43008, 12298, 46083, 13385,
            25606, 28754, 39938, 43008, 36864, 8194, 6146, 39940, 40960, 8195, 39941, 43008, 8196, 6146,
            12308, 6658, 39942, 41280, 47111, 14725, 13447, 25606, 28842, 45064, 6656, 13376, 37120, 9216,
            6147, 12308, 6659, 39945, 41280, 13588, 13383, 25606, 28898, 45066, 6656, 13376, 37120, 9216,
            45067, 36864, 6147, 39945, 40960, 39948, 32769, 39949, 35845, 4096, 13062, 24582, 28970, 45070,
            6656, 13376, 37120, 9216, 6146, 39951, 40960, 6658, 39952, 41280, 13383, 6146, 39953, 40960,
            12551, 24582, 29042, 45074, 6656, 13376, 37120, 9216, 6146, 39955, 40960, 6658, 39956, 41280,
            13383, 25606, 29098, 45077, 6656, 13376, 37120, 9216, 6146, 39958, 40960, 24582, 29138, 45079,
            6656, 13376, 37120, 9216, 6146, 39960, 40960, 24582, 29178, 45081, 6656, 13376, 37120, 9216,
            6147, 39962, 40960, 24582, 29218, 45083, 6656, 13376, 37120, 9216, 6146, 39964, 40960, 6658,
            39965, 41280, 13383, 25606, 29274, 45086, 6656, 13376, 37120, 9216, 6148, 39967, 40960, 12308,
            24582, 29318, 45088, 6656, 13376, 37120, 9216, 6147, 36864, 45065, 36864, 6148, 39967, 32777,
            27654, 29374, 45089, 6656, 13376, 37120, 9216, 6147, 36864, 45082, 36864, 6148, 39967, 32777,
            27654, 29430, 45090, 6656, 13376, 37120, 9216, 45091, 36864, 6148, 39967, 40960, 36864, 39972,
            43008, 39973, 40960, 39974, 40960, 39975, 32773, 39949, 35845, 4096, 13070, 24582, 29530, 45096,
            6656, 13376, 37120, 9216, 6145, 4650, 13383, 37120, 9217, 45097, 8197, 6144, 39978, 40960, 4611,
            13380, 9222, 6150, 4609, 13381, 25606, 29618, 6144, 46123, 13376, 9216, 6150, 4610, 13381, 25606,
            29654, 6144, 46124, 13376, 9216, 4096, 8199, 45101, 8200, 6144, 39978, 40960, 4609, 13377, 9225,
            6153, 4608, 13382, 25606, 30250, 4104, 6663, 5121, 14720, 10247, 5124, 14724, 13442, 9226, 6153,
            36864, 6144, 39982, 32773, 6145, 6666, 13394, 4351, 12559, 13072, 8203, 4104, 6663, 5121, 14720,
            10247, 5124, 14724, 13442, 37120, 9226, 6145, 6666, 13394, 4351, 12559, 36864, 8202, 6155, 6665,
            5121, 14721, 37376, 6656, 39982, 33797, 6666, 14160, 5128, 14737, 13459, 9227, 4104, 6663, 5121,
            14720, 10247, 5124, 14724, 13442, 37120, 9226, 6145, 6666, 13394, 4351, 12559, 36864, 8202, 6155,
            6665, 5122, 14721, 37376, 6656, 39982, 33797, 6666, 14160, 5136, 14737, 13459, 9227, 6149, 6667,
            5183, 14735, 37376, 6664, 39983, 33797, 13504, 9221, 6149, 6667, 5126, 14738, 4671, 13903, 37120,
            6664, 39983, 33797, 13504, 9221, 6149, 6667, 5132, 14738, 4671, 13903, 37120, 6664, 39983, 33797,
            13504, 9221, 6149, 6667, 5138, 14738, 4671, 13903, 37120, 6664, 39983, 33797, 13504, 9221, 6153,
            4611, 13377, 9225, 29692, 7685, 20480
        ]
        self.b = [
            [5, 24, 32],
            [5, 34, 19, 21, 9, 19, 17, 28],
            [45, 6, 31, 18, 19, 0],
            [47, 3, 18, 25, 27, 23, 31, 19, 25],
            [52, 23, 15, 7, 22, 30, 13, 3, 5],
            [21, 53, 16, 23, 30, 15],
            [52, 23, 20, 16],
            [52, 25, 19, 25, 23, 1],
            [74],
            [47, 30, 14, 15, 43, 62, 26, 19, 2],
            [75],
            [50, 21, 28, 29, 16, 17, 14, 24],
            [46, 3, 59, 59, 0, 10, 15, 41, 58, 10, 14],
            [51, 31, 18, 25, 5, 47, 49],
            [72],
            [57, 26, 21, 24, 36, 32, 17, 23, 2, 3, 26],
            [5, 55, 0, 17, 23, 2, 3, 26],
            [5, 24, 55, 0, 17, 23, 2, 3, 26, 20, 10],
            [73],
            [56, 15, 11, 24, 27, 15],
            [24, 47, 11, 24, 27, 15],
            [78],
            [63, 16, 28, 5],
            [79],
            [41, 27, 9, 14, 1],
            [76],
            [45, 10, 31, 30, 14, 3, 7, 11, 15],
            [77],
            [62, 19, 26, 52, 44, 25, 3, 26, 20, 13, 5, 30, 25],
            [62, 19, 26, 52, 44, 25, 3, 26, 20, 13, 5, 30, 25, 53, 52, 25, 2, 30, 5, 27, 24, 17, 15],
            [66],
            [61, 26, 9, 35, 32, 1, 38, 58, 5, 7, 13, 15, 30, 21, 37, 57, 14, 8, 9, 3, 1, 28, 3, 5],
            [67],
            [64],
            [65],
            [1, 45, 23, 13, 5, 7, 11, 93, 91, 20, 19, 25, 32],
            [28, 43, 3, 21, 15, 5, 30, 25],
            [42, 26, 5, 3, 3, 3, 21, 17, 13],
            [46, 3, 36, 63, 30, 3, 31, 17],
            [57, 26, 21, 24],
            [70],
            [],
            [54, 17, 19, 17, 11, 4],
            [90, 24],
            [90],
            [8, 63, 61, 60, 52, 55, 23, 16, 60, 36, 57, 11, 114, 89, 16, 27, 61, 126, 71, 39, 13, 23, 20, 1, 118, 98, 107, 68, 56, 18, 20, 32, 92, 122, 35, 48, 22, 55, 49, 101, 66, 53, 61, 46, 14, 19, 23, 112, 100, 59, 1, 65, 79, 30, 40, 36, 65, 76, 16, 22, 72, 90, 2, 65],
            [57, 19, 17, 11, 41, 52, 19, 25, 60, 45],
            [57, 19, 17, 11, 43, 45]
        ]
        self.F = []
        self.J = {
            0: Func_s,
            1: Func_i,
            2: Func_h,
            3: Func_a,
            4: Func_c,
            5: Func_n,
            6: Func_e,
            7: Func_o,
            8: Func_r,
            9: Func_Q,
            10: Func_C,
            11: Func_B,
            12: Func_f,
            13: Func_g,
            14: Func_u,
            15: Func_w
        }

    def v(self, e, t, n):
        self.C = t or 0

        if "start!" != e:
            self.G = e
            self.b = n or []

        while True:
            print(self.C)
            r = self.G[self.C]
            self.C += 1
            if not isinstance(r, int):
                break

            try:
                self.e(r)
            except Exception as err:
                print(err)

    def e(self, data):
        t = (61440 & data) >> 12
        self.J[t](data).e(self)


def int_overflow(val):
    maxint = 2147483647
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shift(n, i):
    if n < 0:
        n = ctypes.c_uint32(n).value
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)


print(Func_u(7).e(Func_G(), "A7DB7C1C3D89CD761A801BE3577B6048"))
# print(temp_G)
