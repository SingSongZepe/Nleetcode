

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(n: i32, expected: Vec<i32>) {
		let result = Solution::lexical_order(n);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let n = 13;
		let expected = vec![1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9];
		t(n, expected);
	}

	#[test]
	fn test2() {
		let n = 2;
		let expected = vec![1, 2];
		t(n, expected);
	}

	#[test]
	fn test3() {
		let n = 101;
		let expected = vec![1, 10, 100, 101, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 7, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 8, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 9, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99];
		t(n, expected);
	}

}