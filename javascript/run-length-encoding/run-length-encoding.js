"use strict"

export const encode = (sequence) => {
  var currentLetter
  var previousLetter
  var counter = 1
  var encodedSequence = ''
  if (sequence.length > 0) {
    previousLetter = sequence.charAt(0)
		for (var i = 1; i < sequence.length; i++) {
			currentLetter = sequence.charAt(i)
				if (previousLetter !== currentLetter) {
          if (counter > 1) {
					  encodedSequence += counter
          }
					encodedSequence += previousLetter
					counter = 1
				}
				else {
					counter++
				}
			previousLetter = currentLetter
		}
    // Can this be combined with the above code?
    if (counter > 1) {
      encodedSequence += counter
    }
		encodedSequence += previousLetter
  }
  return encodedSequence
}

export const decode = (encodedSequence) => {
  var char
  var sequence = ''
  var repetitions = ''
  if (encodedSequence.length > 0) {
    for (var i = 0; i < encodedSequence.length; i++) {
    	if (isNumber(encodedSequence.charAt(i))) {
    		repetitions += encodedSequence.charAt(i)
    	} else {
        if (!isNumber(encodedSequence.charAt(i + 1)) && repetitions === '') {
          repetitions = '1'
        }
        if (i != 0 && encodedSequence.charAt(i) != encodedSequence.charAt(i - 1)) {
          repetitions = '1'
        }
    		for (var j = 0; j < repetitions; j++) {
    			sequence += encodedSequence.charAt(i)
    		}
    		repetitions = ''
    	}
    }
  }
  return sequence
}

function isNumber(n) {
   return !isNaN(parseFloat(n)) && isFinite(n);
}

//console.log(encode('AAABCCCCCCDDD'))
//console.log(decode('3A1B6C3D'))
