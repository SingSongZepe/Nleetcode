

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(arg: Vec<i32>, expected: i32) {
		let result = Solution::min_operations(arg);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let nums = vec![1, 1, 1];
		let expected = 3;
		t(nums, expected);
	}

	#[test]
	fn test2() {
		let nums = vec![1, 5, 2, 4, 1];
		let expected = 14;
		t(nums, expected);
	}

	#[test]
	fn test3() {
		let nums = vec![0];
		let expected = 0;
		t(nums, expected);
	}

	#[test]
	fn test4() {
		let nums = vec![1, 0];
		let expected = 2;
		t(nums, expected);
	}

}