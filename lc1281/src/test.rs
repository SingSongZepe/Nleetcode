

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(arg: i32, expected: i32) {
		let result = Solution::subtract_product_and_sum(arg);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let n = 234;
		let expected = 15;
		t(n, expected);
	}

	#[test]
	fn test2() {
		let n = 4421;
		let expected = 21;
		t(n, expected);
	}

}