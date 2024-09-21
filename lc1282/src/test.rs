

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(group_sizes: Vec<i32>, expected: Vec<Vec<i32>>) {
		let result = Solution::group_the_people(group_sizes);
		println!("{:?}", result);
		// assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let group_sizes = vec![3, 3, 3, 3, 3, 1, 3];
		let expected = vec![vec![5], vec![0, 1, 2], vec![3, 4, 6]];
		t(group_sizes, expected);
	}

	#[test]
	fn test2() {
		let group_sizes = vec![2, 1, 3, 3, 3, 2];
		let expected = vec![vec![1], vec![0, 5], vec![2, 3, 4]];
		t(group_sizes, expected);
	}
}