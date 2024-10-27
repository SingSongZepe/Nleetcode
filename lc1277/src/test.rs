

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(matrix: Vec<Vec<i32>>, expected: i32) {
		let result = Solution::count_squares(matrix);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		// [
		// 	[0,1,1,1],
		// 	[1,1,1,1],
		// 	[0,1,1,1]
		// ]
		let matrix = vec![vec![0,1,1,1], vec![1,1,1,1], vec![0,1,1,1]];
		let expected = 15;
		t(matrix, expected);
	}

	#[test]
	fn test2() {
		// [
		// 	[1,0,1],
		// 	[1,1,0],
		// 	[1,1,0]
		// ]
		let matrix = vec![vec![1, 0, 1], vec![1, 1, 0], vec![1, 1, 0]];
		let expected = 7;
		t(matrix, expected);
	}
}