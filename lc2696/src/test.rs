

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(s: String, expected: i32) {
		let result = Solution::min_length(s);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}

	fn t1(s: String, expected: i32) {
		let result = Solution1::min_length(s);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let s = "ABFCACDB".to_string();
		let expected = 2;
		t(s, expected);
	}

	#[test]
	fn test2() {
		let s = "ACBBD".to_string();
		let expected = 5;
		t(s, expected);
	}

	#[test]
	fn test11() {
		let s = "ABFCACDB".to_string();
		let expected = 2;
		t1(s, expected);
	}

	#[test]
	fn test21() {
		let s = "ACBBD".to_string();
		let expected = 5;
		t1(s, expected);
	}
}









