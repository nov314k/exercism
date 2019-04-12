function isNumber(n) {
  return !isNaN(parseFloat(n)) && isFinite(n)
}

export const solve = (x, y) => {
      if (isNumber(x) && isNumber(y)) {
    var radius = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2))
    if (radius <= 1) return 10
    else if(radius <= 5) return 5
    else if (radius <= 10) return 1
    else return 0
  } else {
    return null
  }
}
