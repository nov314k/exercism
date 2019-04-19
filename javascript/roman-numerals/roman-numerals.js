var ronums = [
  ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
  ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
  ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
  ['', 'M', 'MM', 'MMM', '?', '?', '?', '?', '?', '?']
]

//export const toRoman = (arabic) => {
  var arabic = 27
  var roman = ''
  var arabicStr = arabic.toString()
  for (var i = arabicStr.length; i > 0; i--) {
    roman = ronums[i - 1][parseInt(arabicStr[i])] + roman
  }
  console.log(roman)
//}
