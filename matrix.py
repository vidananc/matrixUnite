import scipy.io as sio
def getBase16(num):#将读取的10进制数转化为16进制表示的字符串，输入范围为0-15
    if(num < 10):
        return str(num)
    else:
        return chr(65 + num - 10)

def count(matrix):
    dict = {}
    num = 0
    count = 1
    length = len(matrix[0][0])
    matS = ""
    for i in range(1, length + 1):
        for list in matrix:
            for item in list:
                num <<= 1
                num += item[i - 1]
                if(count == 4):
                    matS += getBase16(num)
                    num = 0
                count = count % 4 + 1
        #print(matS)
        if(count != 1):#当前矩阵位数不是4的倍数，将多余的位数作为一个16进制数加上
            num <<= 5 - count
            matS += getBase16(num)
            num = 0
            count = 1
        dict[matS] = dict.get(matS, 0) + 1
        matS = ""
    return dict

path = 'matlab1.mat'
matdata = sio.loadmat(path)
num = 0
matrix = matdata['c']
print(matrix)
dict = count(matrix)
result = ""
with open('result.txt', 'w') as f:
    for items in dict.keys():
        result += "matrix: " + items + "    count: " + str(dict[items])
        result += '\n'
    f.write(result)
    f.close()
