

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(s1: String, s2: String, expected: Vec<String>) {
		let result = Solution::uncommon_from_sentences(s1, s2);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let s1 = "this apple is sweet".to_string();
		let s2 = "this apple is sour".to_string();
		let expected = vec!["sweet".to_string(), "sour".to_string()];
		t(s1, s2, expected);
	}

	#[test]
	fn test2() {
		let s1 = "apple apple".to_string();
		let s2 = "banana".to_string();
		let expected = vec!["banana".to_string()];
		t(s1, s2, expected);
	}

}