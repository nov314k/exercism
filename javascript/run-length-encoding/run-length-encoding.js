encode = (sequence) => {
  "use strict"
  var currentLetter
  var previousLetter
  var counter = 1
  var encodedSequence = ''
  if (sequence.length > 0) {
    previousLetter = sequence.charAt(0)
		for (var i = 1; i < sequence.length; i++) {
			currentLetter = sequence.charAt(i)
				if (previousLetter !== currentLetter) {
					encodedSequence += counter
					encodedSequence += previousLetter
					counter = 1
				}
				else {
					counter++
				}
			previousLetter = currentLetter
		}
		encodedSequence += counter
		encodedSequence += previousLetter
  }
  return encodedSequence
}

console.log(encode('AAABCCCCCCDDD'))

function isNumber(n) {
   return !isNaN(parseFloat(n)) && isFinite(n);
}
//
// var code = '12A3B4C'
// var decoded = ''
// var broj = ''
// for (var i = 0; i < code.length; i++) {
// 	if (isNumber(code.charAt(i))) {
// 		broj += code.charAt(i);
// 	} else {
// 		for (var j = 0; j < broj; j++) {
// 			decoded += code.charAt(i)
// 		}
// 		broj = ''
// 	}
// }
// console.log("Decoded string: ")
// console.log(decoded)
