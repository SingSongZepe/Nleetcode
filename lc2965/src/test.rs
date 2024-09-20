

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(grid: Vec<Vec<i32>>, expected: Vec<i32>) {
		let result = Solution::find_missing_and_repeated_values(grid);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		// grid = [[1,3],[2,2]]
		let grid = vec![ vec![1,3], vec![2,2] ];
		let expected = vec![2, 4];
		t(grid, expected);
	}

	#[test]
	fn test2() {
		// grid = [[9,1,7],[8,9,2],[3,4,6]]
		let grid = vec![ vec![9,1,7], vec![8,9,2], vec![3,4,6] ];
		let expected = vec![9, 5];
		t(grid, expected);
	}

}