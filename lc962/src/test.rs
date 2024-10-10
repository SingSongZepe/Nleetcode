

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(arg: Vec<i32>, expected: i32) {
		let result = Solution::max_width_ramp(arg);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let nums = vec![6, 0, 8, 2, 1, 5];
		let expected = 4;
		t(nums, expected);
	}

	#[test]
	fn test2() {
		let nums = vec![9, 8, 1, 0, 1, 9, 4, 0, 4, 1];
		let expected = 7;
		t(nums, expected);
	}

	#[test]
	fn test3() {
		let nums = vec![1, 2, 1];
		let expected = 2;
		t(nums, expected);
	}
}