

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(sentence: String, expected: bool) {
		let result = Solution::is_circular_sentence(sentence);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let sentence = "leetcode exercises sound delightful".to_string();
		let expected = true;
		t(sentence, expected)
	}

	#[test]
	fn test2() {
		let sentence = "eetcode".to_string();
		let expected = true;
		t(sentence, expected)
	}

	#[test]
	fn test3() {
		let sentence = "Leetcode is cool".to_string();
		let expected = false;
		t(sentence, expected)
	}
}



