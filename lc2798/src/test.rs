

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(hours: Vec<i32>, target: i32, expected: i32) {
		let result = Solution::number_of_employees_who_met_target(hours, target);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let hours = vec![0, 1, 2, 3, 4];
		let target = 2;
		let expected = 3;
		t(hours, target, expected);
	}

	#[test]
	fn test2() {
		let hours = vec![5, 1, 4, 2, 2];
		let target = 6;
		let expected = 0;
		t(hours, target, expected);
	}

}