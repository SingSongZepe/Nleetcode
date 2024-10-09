

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(nums: Vec<i32>, expected: Vec<i32>) {
		let result = Solution::min_subsequence(nums);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let nums = vec![4, 3, 10, 9, 8];
		let expected = vec![10, 9];
		t(nums, expected);
	}

	#[test]
	fn test2() {
		let nums = vec![4, 4, 7, 6, 7];
		let expected = vec![7, 7, 6];
		t(nums, expected);
	}

}