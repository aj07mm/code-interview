exports.palindrome = function (word) {
	var splittedWord = word.split(''),
		end = Math.floor(splittedWord.length / 2);
	for (var i = 0; i <= end; i++) {
		if(splittedWord[i] != splittedWord[splittedWord.length - 1 - i]){
			return false
		}
	};
	return true;
};
