'use strict'

export const encode = (sequence) => {
  var currentLetter
  var previousLetter
  var counter = 1
  var encodedSequence = ''
  if (sequence.length > 0) {
    previousLetter = sequence.charAt(0)
    for (var i = 1; i < sequence.length + 1; i++) {
      currentLetter = sequence.charAt(i)
      if (previousLetter !== currentLetter) {
        if (counter > 1) {
          encodedSequence += counter
        }
        encodedSequence += previousLetter
        counter = 1
      } else {
        counter++
      }
      previousLetter = currentLetter
    }
  }
  return encodedSequence
}

export const decode = (encodedSequence) => {
  var sequence = ''
  var repetitions = ''
  if (encodedSequence.length > 0) {
    for (var i = 0; i < encodedSequence.length; i++) {
      if (isNumber(encodedSequence.charAt(i))) {
        repetitions += encodedSequence.charAt(i)
      } else {
        if (repetitions === '' && encodedSequence.charAt(i) !== encodedSequence.charAt(i - 1)) {
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

function isNumber (n) {
  return !isNaN(parseFloat(n)) && isFinite(n)
}
