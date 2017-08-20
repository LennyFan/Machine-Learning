def kmp(self,a, b):

        # preprocess
        index_b = [0 for i in range(len(b))]
        i,j = 0,0
        while j < len(b):
            # abc abd abd abc abc
            # 000 120 120 123 453

            # init
            if j == i:
                index_b[j] = 0
                j += 1
                i  = 0
                continue

            if b[i] == b[j]:
                index_b[j] = i+1
                i += 1
                j += 1
            elif i != 0 and b[i-1] != 0:
                i = index_b[i-1]
            else:
                index_b[j] = 0
                j += 1
                i = 1


        i,j = 0,0
        while i < len(a):
            if a[i] == b[j]:
                i += 1
                j += 1
            elif j != 0 : # a[i] != b[j]
                j = index_b[j-1]
            else: # a[i] != b[0] ****** boundary
                i += 1

            if j == len(b):
                return True

        return False
