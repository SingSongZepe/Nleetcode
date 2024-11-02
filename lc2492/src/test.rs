

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(n: i32, roads: Vec<Vec<i32>>, expected: i32) {
		let result = Solution::min_score(n, roads);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let n = 4;
		let roads = vec![vec![1,2,9],vec![2,3,6],vec![2,4,5],vec![1,4,7]];
		let expected = 5;
		t(n, roads, expected)
	}

	#[test]
	fn test2() {
		let n = 2;
		let roads = vec![vec![1,2,2],vec![1,3,4],vec![3,4,7]];
		let expected = 2;
		t(n, roads, expected)
	}

}