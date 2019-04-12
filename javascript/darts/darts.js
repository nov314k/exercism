function isNumber (n) {
  return !isNaN(parseFloat(n)) && isFinite(n)
}

export const solve = (x, y) => {
  var points = null
  if (isNumber(x) && isNumber(y)) {
    var biggerCoordinate = Math.max(x, y)
    if (biggerCoordinate <= 1) {
      points = 10
    } else if (biggerCoordinate <= 5) {
      points = 5
    } else if (biggerCoordinate <= 10) {
      points = 1
    } else {
      points = 0
    }
  }
  return points
}
