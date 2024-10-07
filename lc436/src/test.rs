

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(intervals: Vec<Vec<i32>>, expected: Vec<i32>) {
		let result = Solution::find_right_interval(intervals);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let intervals = vec![vec![1, 2]];
		let expected = vec![-1];
		t(intervals, expected);
	}

	#[test]
	fn test2() {
		let intervals = vec![vec![3, 4], vec![2, 3], vec![1, 2]];
		let expected = vec![-1, 0, 1];
		t(intervals, expected);
	}

	#[test]
	fn test3() {
		let intervals = vec![vec![1, 4], vec![2, 3], vec![3, 4]];
		let expected = vec![-1, 2, -1];
		t(intervals, expected);
	}
}