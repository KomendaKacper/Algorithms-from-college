class Matrix:
  def __mul__(self, matrix2):
    if self.size()[1] != matrix2.size()[0]:
      return ("Bledny rozmiar macierzy")
    
    rows = self.size()[0]
    columns = matrix2.size()[1]
    result = Matrix((rows, columns))

    for i in range(rows):
      for j in range(columns):
        for k in range(matrix2.size()[0]):
            result.matrix[i][j] += self.matrix[i][k] * matrix2.matrix[k][j]
    return result

  def __getitem__(self, item):
    return self.matrix[item]

  def __setitem__(self, key, value):
    self.matrix[key] = value

  def size(self):
    rows_size = len(self.matrix)
    columns_size = len(self.matrix[0])
    return rows_size, columns_size

  def __init__(self, matrix, zero = 0): #konstruktor
    if isinstance(matrix, tuple):
      self.matrix = []
      for i in range(matrix[0]):
        row = []
        for j in range(matrix[1]):
          row.append(zero)
        self.matrix.append(row)
    else:
      self.matrix = matrix  

  def __str__(self):
    s = ''
    for i in range(len(self.matrix)):
      s += ("|")
      for j in range(len(self.matrix[i])-1):
        s += str(self.matrix[i][j]) + " "
      s += str(self.matrix[i][j+1]) + "|\n"
    return s

  def __add__(self, matrix2):
    rows = self.size()[0]
    columns = self.size()[1]

    if self.size() != matrix2.size():
      return ('Rozny rozmiar macierzy')

    result = Matrix((rows,columns))

    for i in range(rows):
      for j in range(columns):
        result.matrix[i][j] += self.matrix[i][j] + matrix2.matrix[i][j]

    return result
  
def transpose(matrix):
  rows_size, columns_size = matrix.size()
  result = Matrix((columns_size, rows_size))

  for i in range(rows_size):
      for j in range(columns_size):
          result[j][i] = matrix[i][j]

  return result

def chio(matrix):
    s = 1
    while matrix.size()[0] > 2:
        rows_size, columns_size = matrix.size()
        if matrix[0][0] == 0:
            temp = matrix[0]
            for i in range (1, rows_size):
                if matrix[i][0] != 0:
                    matrix[0] = matrix[i]
                    matrix[i] = temp
                    s = -1
                    break
        s *= 1/(matrix[0][0]**(matrix.size()[0]-2))
        result = Matrix((rows_size-1, columns_size-1))
        for i in range (rows_size - 1):
            for j in range (columns_size - 1):
                result[i][j] = matrix[0][0]*matrix[i+1][j+1]-matrix[0][j+1]*matrix[i+1][0]
        matrix = result
    m = (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]) * s
    return m



def main():
  m1 = Matrix(
  [
[5 , 1 , 1 , 2 , 3],
[4 , 2 , 1 , 7 , 3],
[2 , 1 , 2 , 4 , 7],
[9 , 1 , 0 , 7 , 0],
[1 , 4 , 7 , 2 , 2]
]
  )

  m2 = Matrix(
  [
[0 , 1 , 1 , 2 , 3],
[4 , 2 , 1 , 7 , 3],
[2 , 1 , 2 , 4 , 7],
[9 , 1 , 0 , 7 , 0],
[1 , 4 , 7 , 2 , 2]
]
  )
#   print (chio(m1))
  print (chio(m2))
  
if __name__ == "__main__":
    main()